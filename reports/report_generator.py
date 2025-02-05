import pandas as pd
import matplotlib.pyplot as plt
from config.db_config import get_db_connection
from utils.logger import log_user_action

class ReportGenerator:
    def __init__(self):
        self.conn = get_db_connection()

    def generate_monthly_report(self, month, year):
        query = "SELECT * FROM expenses WHERE EXTRACT(MONTH FROM date) = %s AND EXTRACT(YEAR FROM date) = %s"
        df = pd.read_sql(query, self.conn, params=(month, year))

        if df.empty:
            print("No expenses found for the given month and year.")
            return

        df.to_csv(f"monthly_report_{month}_{year}.csv", index=False)
        print("Report generated successfully!")

    def plot_expense_by_category(self, month, year):
        query = "SELECT category, SUM(amount) FROM expenses WHERE EXTRACT(MONTH FROM date) = %s AND EXTRACT(YEAR FROM date) = %s GROUP BY category"
        df = pd.read_sql(query, self.conn, params=(month, year))

        if df.empty:
            print("No expenses to visualize.")
            return

        plt.figure(figsize=(8, 6))
        plt.pie(df["sum"], labels=df["category"], autopct='%1.1f%%')
        plt.title(f"Expense Distribution - {month}/{year}")
        plt.savefig(f"expense_pie_chart_{month}_{year}.png")
        plt.show()

    def view_reports(self, month, year):
        query = "SELECT * FROM expenses WHERE EXTRACT(MONTH FROM date) = %s AND EXTRACT(YEAR FROM date) = %s"
        df = pd.read_sql(query, self.conn, params=(month, year))

        if df.empty:
            print("No expenses found for the given month and year.")
            return

        log_user_action(f"Viewed expense report for {month}/{year}")
        print(df)

    def generate_report(self):
        query = "SELECT category, SUM(amount) FROM expenses GROUP BY category"
        df = pd.read_sql(query, self.conn)

        if df.empty:
            print("No expenses found to generate a report.")
            return

        plt.figure(figsize=(8, 6))
        plt.pie(df["sum"], labels=df["category"], autopct='%1.1f%%')
        plt.title("Expense Distribution")
        plt.savefig("expense_report.png")
        plt.show()
        
        log_user_action("Generated an expense report")
        print("Report generated successfully!")
