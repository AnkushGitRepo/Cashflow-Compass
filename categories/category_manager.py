import psycopg2
from config.db_config import get_db_connection
from datetime import datetime, timedelta
from utils.logger import log_user_action

class CategoryManager:
    def __init__(self):
        self.conn = get_db_connection()

    def display_categories(self, user_id):
        """Show all unique categories available to the user with 6 per line."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT DISTINCT category_name FROM categories WHERE user_id = %s OR user_id IS NULL", (user_id,))
                categories = cur.fetchall()

                if not categories:
                    print("⚠️ No categories found. Please create a category first.")
                    return

                print("\n--- Available Categories ---\n")
                unique_categories = sorted(set(cat[0] for cat in categories))  # Ensure uniqueness and sorted order
                
                # Print 6 categories per line
                for i in range(0, len(unique_categories), 6):
                    print("   ".join(f"{cat:<15}" for cat in unique_categories[i:i+6]))  
                print("\n")

                # Log the action in user_logs
                log_user_action(user_id, f"Viewed all available categories.")
                
        except Exception as e:
            print(f"⚠️ Error fetching categories: {e}")

    def show_spending_last_30_days(self, user_id):
        """Show category-wise spending for the past 30 days in a custom table format."""
        try:
            start_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT c.category_name, SUM(e.amount) AS total_spent
                    FROM expenses e
                    JOIN categories c ON e.category_id = c.id
                    WHERE e.user_id = %s AND e.date >= %s
                    GROUP BY c.category_name
                    ORDER BY total_spent DESC;
                """, (user_id, start_date))

                spending = cur.fetchall()

                if not spending:
                    print("⚠️ No spending data available for the last 30 days.")
                    return

                # Calculate total spending
                total_spent = sum(row[1] for row in spending)

                # Print table header
                print("\n--- Last 30 Days' Spending ---\n")
                print(f"{'Category':<20} {'Total Spent':>15}")
                print("=" * 40)

                # Print table rows
                for category, amount in spending:
                    print(f"{category:<20} ${amount:>13.2f}")

                print("=" * 40)
                print(f"{'Total':<20} ${total_spent:>13.2f}\n")
                
                # Log the action in user_logs
                log_user_action(user_id, f"Viewed spending data for the last 30 days.")
        except Exception as e:
            print(f"⚠️ Error retrieving spending data: {e}")

    def manage_categories(self, user_id):
        """Menu for managing categories."""
        while True:
            print("\n--- Category Management ---")
            print("1. View Categories")
            print("2. View Last 30 Days' Spending")
            print("3. Create New Category")
            print("4. Delete Category")
            print("5. Go Back")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.display_categories(user_id)
            elif choice == "2":
                self.show_spending_last_30_days(user_id)
            elif choice == "3":
                self.create_category(user_id)
            elif choice == "4":
                self.delete_category(user_id)
            elif choice == "5":
                break
            else:
                print("⚠️ Invalid option. Please choose a valid number (1-5).")

    def create_category(self, user_id):
        """Allow users to create a new category, ensuring uniqueness and proper formatting."""
        while True:
            category_name = input("Enter new category name: ").strip().capitalize()  # Ensure capitalization

            if not category_name:
                print("⚠️ Category name cannot be empty.")
                continue

            try:
                with self.conn.cursor() as cur:
                    # Check if the category already exists for the user
                    cur.execute("SELECT 1 FROM categories WHERE user_id = %s AND LOWER(category_name) = LOWER(%s)", 
                                (user_id, category_name))
                    if cur.fetchone():
                        print(f"⚠️ The category '{category_name}' already exists. Please choose a different name.")
                        continue

                    # Insert new category
                    cur.execute("INSERT INTO categories (user_id, category_name, is_predefined) VALUES (%s, %s, FALSE)", 
                                (user_id, category_name))
                    self.conn.commit()

                    # Log the creation in user_logs
                    log_user_action(user_id, f"Created category named '{category_name}'.")
                    print(f"✅ Category '{category_name}' created successfully!")
                    break  # Exit loop after successful creation

            except Exception as e:
                print(f"⚠️ Error creating category: {e}")

    def delete_category(self, user_id):
        """Allow users to delete their own created categories and remove all associated expenses."""
        try:
            with self.conn.cursor() as cur:
                # Fetch only user-created categories (predefined categories cannot be deleted)
                cur.execute("SELECT category_name FROM categories WHERE user_id = %s AND is_predefined = FALSE", (user_id,))
                categories = cur.fetchall()

                if not categories:
                    print("⚠️ No user-created categories available to delete.")
                    return

                print("\n--- Your Custom Categories ---")
                category_list = [cat[0] for cat in categories]
                
                for i, category in enumerate(category_list, start=1):
                    print(f"{i}. {category}")
                
                while True:
                    choice = input("Enter the category number to delete (or type 'cancel' to go back): ").strip()

                    if choice.lower() == "cancel":
                        return

                    if choice.isdigit():
                        choice_index = int(choice) - 1
                        if 0 <= choice_index < len(category_list):
                            category_to_delete = category_list[choice_index]
                            break
                        else:
                            print("⚠️ Invalid selection. Please enter a valid number.")
                    else:
                        print("⚠️ Invalid input. Please enter a number.")

                # Delete category and associated expenses
                cur.execute("DELETE FROM expenses WHERE category_id = (SELECT id FROM categories WHERE user_id = %s AND category_name = %s)", 
                            (user_id, category_to_delete))
                cur.execute("DELETE FROM categories WHERE user_id = %s AND category_name = %s", 
                            (user_id, category_to_delete))
                self.conn.commit()

                # Log the deletion in user_logs
                log_user_action(user_id, f"Deleted category '{category_to_delete}' and all associated expenses.")

                print(f"✅ Category '{category_to_delete}' and all associated expenses have been deleted successfully!")

        except Exception as e:
            print(f"⚠️ Error deleting category: {e}")