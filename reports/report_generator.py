import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from config.db_config import get_db_connection
from utils.logger import log_user_action


class ReportGenerator:
    def __init__(self):
        self.conn = get_db_connection()

    def generate_pdf_report(self, user_id):
        """Generate a detailed PDF report."""
        from utils.pdf_generator import PDFGenerator  # ✅ Import inside the function to avoid circular import
        pdf_generator = PDFGenerator()
        pdf_generator.generate_pdf_report(user_id)

    def view_reports(self, user_id):
        """Display report options and generate the selected report."""
        print("\n--- View Reports ---")
        print("1. Daily Report")
        print("2. Weekly Report")
        print("3. Monthly Report")
        print("4. Yearly Report")
        print("5. Comparison Report (Current vs. Previous Year)")
        print("6. Cancel")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            date_str = input("Enter the date (YYYY-MM-DD): ").strip()
            self.generate_daily_report(user_id, date_str)
        elif choice == "2":
            start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
            self.generate_weekly_report(user_id, start_date)
        elif choice == "3":
            month = input("Enter month (1-12): ").strip()
            year = input("Enter year (YYYY): ").strip()
            self.generate_monthly_report(user_id, month, year)
        elif choice == "4":
            year = input("Enter year (YYYY): ").strip()
            self.generate_yearly_report(user_id, year)
        elif choice == "5":
            self.generate_comparison_report(user_id)
        elif choice == "6":
            return
        else:
            print("Invalid choice.")

    def fetch_expense_data(self, user_id, query, params):
        """Fetch expense data and return a DataFrame."""
        try:
            df = pd.read_sql(query, self.conn, params=params)
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def generate_subplots(self, df_pie, df_bar, title):
        """Generate a subplot with a pie chart and a bar chart."""
        if df_pie.empty:
            print("No data available.")
            return

        fig, axes = plt.subplots(1, 2, figsize=(12, 5))

        # Pie Chart
        axes[0].pie(df_pie["total_spent"], labels=df_pie["category_name"], autopct="%1.1f%%")
        axes[0].set_title(f"{title} - Pie Chart")

        # Bar Chart
        axes[1].bar(df_bar["category_name"], df_bar["total_spent"], color='blue')
        axes[1].set_xlabel("Category")
        axes[1].set_ylabel("Total Spent")
        axes[1].set_title(f"{title} - Bar Chart")
        axes[1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()

    def generate_daily_report(self, user_id, date):
        """Generate a daily expense report with subplots."""
        query = """
            SELECT c.category_name, SUM(e.amount) AS total_spent
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            WHERE e.user_id = %s AND e.date = %s
            GROUP BY c.category_name;
        """
        df = self.fetch_expense_data(user_id, query, (user_id, date))

        if df is not None:
            log_user_action(user_id, f"Generated daily report for {date}")
            self.generate_subplots(df, df, f"Daily Expenses - {date}")

    def generate_weekly_report(self, user_id, start_date):
        """Generate a weekly expense report with subplots."""
        end_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=6)
        query = """
            SELECT c.category_name, SUM(e.amount) AS total_spent
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            WHERE e.user_id = %s AND e.date BETWEEN %s AND %s
            GROUP BY c.category_name;
        """
        df = self.fetch_expense_data(user_id, query, (user_id, start_date, end_date))

        if df is not None:
            log_user_action(user_id, f"Generated weekly report for {start_date} to {end_date.date()}")
            self.generate_subplots(df, df, f"Weekly Expenses ({start_date} - {end_date.date()})")

    def generate_monthly_report(self, user_id, month, year):
        """Generate a monthly expense report with subplots."""
        query = """
            SELECT c.category_name, SUM(e.amount) AS total_spent
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            WHERE e.user_id = %s AND EXTRACT(MONTH FROM e.date) = %s AND EXTRACT(YEAR FROM e.date) = %s
            GROUP BY c.category_name;
        """
        df = self.fetch_expense_data(user_id, query, (user_id, month, year))

        if df is not None:
            log_user_action(user_id, f"Generated monthly report for {month}/{year}")
            self.generate_subplots(df, df, f"Monthly Expenses - {month}/{year}")

    def generate_yearly_report(self, user_id, year):
        """Generate a yearly expense report with subplots."""
        query = """
            SELECT c.category_name, SUM(e.amount) AS total_spent
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            WHERE e.user_id = %s AND EXTRACT(YEAR FROM e.date) = %s
            GROUP BY c.category_name;
        """
        df = self.fetch_expense_data(user_id, query, (user_id, year))

        if df is not None:
            log_user_action(user_id, f"Generated yearly report for {year}")
            self.generate_subplots(df, df, f"Yearly Expenses - {year}")

    def generate_comparison_report(self, user_id):
        """Generate a grouped bar chart for previous vs. current year's monthly expenses with correctly formatted X-axis labels."""
        query = """
            SELECT EXTRACT(MONTH FROM e.date) AS month, EXTRACT(YEAR FROM e.date) AS year, SUM(e.amount) AS total_spent
            FROM expenses e
            WHERE e.user_id = %s AND EXTRACT(YEAR FROM e.date) IN (%s, %s)
            GROUP BY year, month
            ORDER BY year, month;
        """
        current_year = datetime.today().year
        previous_year = current_year - 1

        df = self.fetch_expense_data(user_id, query, (user_id, previous_year, current_year))

        if df is not None:
            log_user_action(user_id, f"Generated yearly comparison report for {previous_year} vs {current_year}")

            # Pivot data for proper plotting
            df_pivot = df.pivot(index="month", columns="year", values="total_spent").fillna(0)

            # Generate correct X-axis labels (e.g., "Jan-2024", "Jan-2025", "Feb-2024", "Feb-2025", ...)
            month_labels = []
            for month in df_pivot.index:
                month_name = datetime(2000, int(month), 1).strftime('%b')  # Convert month number to name (e.g., "Jan")
                month_labels.append(f"{month_name}-{previous_year}")
                month_labels.append(f"{month_name}-{current_year}")

            # Flatten data for bar plotting
            values = []
            for month in df_pivot.index:
                values.append(df_pivot.loc[month, previous_year])
                values.append(df_pivot.loc[month, current_year])

            # Creating the grouped bar chart
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.bar(month_labels, values, color=['#1f77b4', '#ff7f0e'] * len(df_pivot.index), width=0.6)

            ax.set_xlabel("Month")
            ax.set_ylabel("Total Spent")
            ax.set_title(f"Comparison Report: {previous_year} vs {current_year}")
            ax.tick_params(axis='x', rotation=45)
            plt.show()
