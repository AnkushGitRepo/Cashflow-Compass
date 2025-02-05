import psycopg2
from config.db_config import get_db_connection
from utils.logger import log_user_action

class ExpenseManager:
    def __init__(self):
        self.conn = get_db_connection()
    

    def add_expense(self, amount, category_name, description, date):
        try:
            with self.conn.cursor() as cur:
                # Fetch the category_id from the categories table
                cur.execute("SELECT id FROM categories WHERE category_name = %s", (category_name,))
                category = cur.fetchone()

                if category is None:
                    print(f"Error: Category '{category_name}' does not exist.")
                    return

                category_id = category[0]

                # Insert the expense with the correct category_id
                cur.execute(
                    "INSERT INTO expenses (amount, category_id, description, date) VALUES (%s, %s, %s, %s)",
                    (amount, category_id, description, date)
                )
                self.conn.commit()
                print("Expense added successfully!")

        except Exception as e:
            print(f"Error: {e}")

    def delete_expense(self, expense_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))
                self.conn.commit()
                print("Expense deleted successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def update_expense(self, expense_id, new_amount, new_category, new_description, new_date):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE expenses 
                    SET amount = %s, category = %s, description = %s, date = %s 
                    WHERE id = %s
                """, (new_amount, new_category, new_description, new_date, expense_id))
                self.conn.commit()
                log_user_action(f"Updated expense with ID {expense_id}")
                print("Expense updated successfully!")
        except Exception as e:
            print(f"Error: {e}")

    def search_expenses(self, category=None, start_date=None, end_date=None):
        try:
            query = "SELECT * FROM expenses WHERE TRUE"
            params = []

            if category:
                query += " AND category = %s"
                params.append(category)
            if start_date and end_date:
                query += " AND date BETWEEN %s AND %s"
                params.append(start_date)
                params.append(end_date)

            with self.conn.cursor() as cur:
                cur.execute(query, tuple(params))
                results = cur.fetchall()
                for row in results:
                    print(row)
        except Exception as e:
            print(f"Error: {e}")
