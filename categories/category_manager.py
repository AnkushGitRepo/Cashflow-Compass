import psycopg2
from config.db_config import get_db_connection
from datetime import datetime, timedelta
from utils.logger import log_user_action

class CategoryManager:
    def __init__(self):
        self.conn = get_db_connection()

    def display_categories(self):
        """Show all categories available to the user."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT category_name FROM categories")
                categories = cur.fetchall()

                if not categories:
                    print("No categories found.")
                    return

                print("\n--- Available Categories ---")
                for category in categories:
                    print(f"- {category[0]}")

        except Exception as e:
            print(f"Error fetching categories: {e}")

    def show_spending_last_30_days(self):
        """Show category-wise spending for the past 30 days."""
        try:
            start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT category, SUM(amount) 
                    FROM expenses 
                    WHERE date >= %s 
                    GROUP BY category
                """, (start_date,))
                spending = cur.fetchall()

                if not spending:
                    print("No spending data available for the last 30 days.")
                    return

                print("\n--- Spending in the Last 30 Days ---")
                print(f"{'Category'.ljust(20)} | {'Total Spent'}")
                print("-" * 40)
                for category, amount in spending:
                    print(f"{category.ljust(20)} | {amount}")
                print("-" * 40)

        except Exception as e:
            print(f"Error retrieving spending data: {e}")

    def create_category(self):
        """Allow users to create a new category."""
        category_name = input("Enter new category name: ").strip()

        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM categories WHERE category_name = %s", (category_name,))
                if cur.fetchone():
                    print("Category already exists!")
                    return

                cur.execute("INSERT INTO categories (category_name) VALUES (%s)", (category_name,))
                self.conn.commit()
                log_user_action(f"Created a new category: {category_name}")
                print(f"Category '{category_name}' created successfully!")

        except Exception as e:
            print(f"Error creating category: {e}")

    def delete_category(self):
        """Allow users to delete a category."""
        category_name = input("Enter category name to delete: ").strip()

        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT 1 FROM categories WHERE category_name = %s", (category_name,))
                if not cur.fetchone():
                    print("Category does not exist!")
                    return

                cur.execute("DELETE FROM categories WHERE category_name = %s", (category_name,))
                self.conn.commit()
                log_user_action(f"Deleted category: {category_name}")
                print(f"Category '{category_name}' deleted successfully!")

        except Exception as e:
            print(f"Error deleting category: {e}")

    

    def manage_categories(self):
        """Menu for managing categories."""
        while True:
            print("\n--- Category Management ---\n")
            print("1. View Categories")
            print("2. View Last 30 Days' Spending")
            print("3. Create New Category")
            print("4. Delete Category")
            print("5. Go Back")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.display_categories()
            elif choice == "2":
                self.show_spending_last_30_days()
            elif choice == "3":
                self.create_category()
            elif choice == "4":
                self.delete_category()
            elif choice == "5":
                break
            else:
                print("Invalid option.")
