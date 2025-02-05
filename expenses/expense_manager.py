import psycopg2
from config.db_config import get_db_connection
from utils.logger import log_user_action
from datetime import datetime, timedelta

class ExpenseManager:
    def __init__(self):
        self.conn = get_db_connection()
    

    def fetch_categories(self, user_id):
        """Fetch all categories for a user and return as a list of tuples (id, name)."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id, category_name FROM categories WHERE user_id = %s OR user_id IS NULL", (user_id,))
                return cur.fetchall()
        except Exception as e:
            print(f"Error fetching categories: {e}")
            return []
        
    
    def add_expense(self, user_id):
        """Allow users to add expenses with formatted category display and improved input handling."""
        categories = self.fetch_categories(user_id)

        if not categories:
            print("No categories available. Please create a category first.")
            return

        # Ask for amount first
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid amount. Enter a valid number.")

        # Display categories properly formatted across the terminal
        print("\n--- Available Categories ---")
        max_length = max(len(cat_name) for _, cat_name in categories) + 5  # Padding for alignment
        columns = 6  # Number of columns per row

        for i, (cat_id, cat_name) in enumerate(categories, start=1):
            print(f"{i}. {cat_name.ljust(max_length)}", end="  ")
            if i % columns == 0:
                print()  # New line after every 'columns' categories
        print("\n")

        # Allow category selection by name or number
        while True:
            category_input = input("Enter category name or number: ").strip().lower()

            if category_input.isdigit():
                category_index = int(category_input) - 1
                if 0 <= category_index < len(categories):
                    category_id, category_name = categories[category_index]
                    break
                else:
                    print("Invalid category number. Please enter a valid number.")
            else:
                matched_category = next((cat for cat in categories if cat[1].lower() == category_input), None)
                if matched_category:
                    category_id, category_name = matched_category
                    break
                else:
                    print("Invalid category name. Please enter a valid category.")

        # Default description is the category name
        description = input(f"Enter description (Press Enter to use '{category_name}'): ").strip()
        if not description:
            description = category_name

        # Restrict date input (allow skipping by pressing Enter)
        today = datetime.today()
        min_date = today - timedelta(days=180)
        max_date = today + timedelta(days=180)

        while True:
            date_str = input(f"Enter date (YYYY-MM-DD) (Press Enter for {today.date()}): ").strip()
            if not date_str:
                expense_date = today  # Use current date if skipped
                break

            try:
                expense_date = datetime.strptime(date_str, "%Y-%m-%d")
                if min_date <= expense_date <= max_date:
                    break
                else:
                    print(f"Invalid date. Enter a date between {min_date.date()} and {max_date.date()}.")
            except ValueError:
                print("Invalid format. Use YYYY-MM-DD.")

        # Insert expense into the database with error handling
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO expenses (user_id, category_id, amount, description, date) VALUES (%s, %s, %s, %s, %s)",
                    (user_id, category_id, amount, description, expense_date.date())
                )
                self.conn.commit()
                log_user_action(user_id, f"Added expense: {amount} in '{category_name}'.")
                print("Expense added successfully!")
        except Exception as e:
            log_user_action(user_id, f"Error adding expense: {e}")  # Log error
            print(f"Error adding expense: {e}")  # Print error for debugging


    def search_expenses(self, user_id):
        """Allow the user to search expenses by category or date."""
        search_query = "SELECT e.id, e.amount, c.category_name, e.description, e.date FROM expenses e JOIN categories c ON e.category_id = c.id WHERE e.user_id = %s"
        params = [user_id]

        print("\n--- Search Expense Options ---")
        print("1. Search by Category")
        print("2. Search by Date Range")
        print("3. Show All Expenses")
        print("4. Cancel")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            category_name = input("Enter category name: ").strip().lower()
            search_query += " AND LOWER(c.category_name) = %s"
            params.append(category_name)
        elif choice == "2":
            start_date = input("Enter start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter end date (YYYY-MM-DD): ").strip()
            search_query += " AND e.date BETWEEN %s AND %s"
            params.extend([start_date, end_date])
        elif choice == "3":
            pass  # Show all expenses
        elif choice == "4":
            return []  # Cancel search
        else:
            print("Invalid choice.")
            return []

        try:
            with self.conn.cursor() as cur:
                cur.execute(search_query, tuple(params))
                expenses = cur.fetchall()
                if expenses:
                    log_user_action(user_id, f"Viewed expenses with filter: {choice}")
                return expenses
        except Exception as e:
            print(f"Error retrieving expenses: {e}")
            return []

    def delete_expense(self, user_id):
        """Delete an expense after displaying filtered search results."""
        expenses = self.search_expenses(user_id)

        if not expenses:
            print("No expenses found.")
            return

        # Display expenses in a table-like structure
        print("\n--- Matching Expenses ---")
        print(f"{'ID'.ljust(5)} {'Amount'.ljust(10)} {'Category'.ljust(15)} {'Description'.ljust(30)} {'Date'}")
        print("-" * 80)

        for exp_id, amount, category, description, date in expenses:
            print(f"{str(exp_id).ljust(5)} {str(amount).ljust(10)} {category.ljust(15)} {description.ljust(30)} {date}")

        print("-" * 80)

        # Ask user to enter an expense ID to delete
        while True:
            expense_id = input("Enter the Expense ID to delete (or type 'cancel' to go back): ").strip()
            if expense_id.lower() == "cancel":
                return

            if expense_id.isdigit() and any(int(expense_id) == exp[0] for exp in expenses):
                try:
                    with self.conn.cursor() as cur:
                        cur.execute("DELETE FROM expenses WHERE id = %s AND user_id = %s", (expense_id, user_id))
                        self.conn.commit()
                        log_user_action(user_id, f"Deleted expense ID {expense_id}")
                        print(f"Expense ID {expense_id} deleted successfully!")
                    break
                except Exception as e:
                    print(f"Error deleting expense: {e}")
                    break
            else:
                print("Invalid Expense ID. Please select a valid ID from the list.")

    def update_expense(self, user_id):
        """Update an expense after displaying filtered search results."""
        expenses = self.search_expenses(user_id)

        if not expenses:
            print("No expenses found.")
            return

        # Display expenses in a table-like structure
        print("\n--- Matching Expenses ---")
        print(f"{'ID'.ljust(5)} {'Amount'.ljust(10)} {'Category'.ljust(15)} {'Description'.ljust(30)} {'Date'}")
        print("-" * 80)

        for exp_id, amount, category, description, date in expenses:
            print(f"{str(exp_id).ljust(5)} {str(amount).ljust(10)} {category.ljust(15)} {description.ljust(30)} {date}")

        print("-" * 80)

        # Ask user to enter an expense ID to update
        while True:
            expense_id = input("Enter the Expense ID to update (or type 'cancel' to go back): ").strip()
            if expense_id.lower() == "cancel":
                return

            if expense_id.isdigit() and any(int(expense_id) == exp[0] for exp in expenses):
                expense_id = int(expense_id)
                break
            else:
                print("Invalid Expense ID. Please select a valid ID from the list.")

        # Ask user for new details (allow skipping fields)
        print("\n--- Update Expense ---")

        # Handle amount input (allow skipping)
        new_amount = input("Enter new amount (or press Enter to keep unchanged): ").strip()
        new_amount = float(new_amount) if new_amount else None

        # Fetch categories for updating
        categories = self.fetch_categories(user_id)

        # Display categories inline
        print("\n--- Available Categories ---")
        max_length = max(len(cat_name) for _, cat_name in categories) + 3
        columns = 4
        for i, (cat_id, cat_name) in enumerate(categories, start=1):
            print(f"{i}. {cat_name.ljust(max_length)}", end="  ")
            if i % columns == 0:
                print()
        print("\n")

        # Handle category input (allow skipping)
        category_input = input("Enter new category name or number (Press Enter to keep unchanged): ").strip().lower()
        if category_input:
            if category_input.isdigit():
                category_index = int(category_input) - 1
                if 0 <= category_index < len(categories):
                    new_category_id = categories[category_index][0]
                else:
                    print("Invalid category number. Keeping unchanged.")
                    new_category_id = None
            else:
                matched_category = next((cat for cat in categories if cat[1].lower() == category_input), None)
                new_category_id = matched_category[0] if matched_category else None
        else:
            new_category_id = None

        # Handle description input (allow skipping)
        new_description = input("Enter new description (or press Enter to keep unchanged): ").strip()
        new_description = new_description if new_description else None

        # Handle date input (allow skipping)
        today = datetime.today()
        min_date = today - timedelta(days=180)
        max_date = today + timedelta(days=180)

        date_str = input("Enter new date (YYYY-MM-DD) (Press Enter to keep unchanged): ").strip()
        if date_str:
            try:
                new_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                if not (min_date.date() <= new_date <= max_date.date()):
                    print(f"Invalid date. Keeping unchanged.")
                    new_date = None
            except ValueError:
                print("Invalid format. Keeping unchanged.")
                new_date = None
        else:
            new_date = None

        # ✅ Prevent empty update query
        if not any([new_amount, new_category_id, new_description, new_date]):
            print("No changes made. Expense remains unchanged.")
            return

        # ✅ Build and execute the update query dynamically
        try:
            with self.conn.cursor() as cur:
                update_query = "UPDATE expenses SET"
                update_values = []
                if new_amount is not None:
                    update_query += " amount = %s,"
                    update_values.append(new_amount)
                if new_category_id is not None:
                    update_query += " category_id = %s,"
                    update_values.append(new_category_id)
                if new_description is not None:
                    update_query += " description = %s,"
                    update_values.append(new_description)
                if new_date is not None:
                    update_query += " date = %s,"
                    update_values.append(new_date)

                update_query = update_query.rstrip(',') + " WHERE id = %s AND user_id = %s"
                update_values.extend([expense_id, user_id])

                cur.execute(update_query, tuple(update_values))
                self.conn.commit()
                log_user_action(user_id, f"Updated expense ID {expense_id}")
                print(f"Expense ID {expense_id} updated successfully!")
        except Exception as e:
            log_user_action(user_id, f"Error updating expense ID {expense_id}")
            print(f"Error updating expense: {e}")
