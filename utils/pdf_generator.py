from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
from datetime import datetime
from config.db_config import get_db_connection
from utils.logger import log_user_action

class PDFGenerator(FPDF):
    """Class to generate detailed PDF reports of expenses."""

    def __init__(self):
        super().__init__()
        self.conn = get_db_connection()

    def fetch_expense_data(self, user_id):
        """Fetch all expense data for the given user."""
        query = """
            SELECT e.id, c.category_name, e.amount, e.description, e.date
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            WHERE e.user_id = %s
            ORDER BY e.date ASC;
        """
        try:
            return pd.read_sql(query, self.conn, params=(user_id,))
        except Exception as e:
            print(f"Error fetching expense data: {e}")
            return None

    def generate_expense_graphs(self, df, user_id):
        """Generate and save full-page expense graphs."""
        if df.empty:
            return None, None, None
        
        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.to_period("M")

        # Group data by category and month
        category_df = df.groupby(["month", "category_name"])["amount"].sum().unstack(fill_value=0)

        # Expense Trend Graph (Full Page)
        trend_chart_path = f"expense_trend_chart_{user_id}.png"
        plt.figure(figsize=(16, 12))  # ✅ Full Page
        category_df.plot(kind="line", marker="o", figsize=(16, 10))
        plt.xlabel("Month", fontsize=16)
        plt.ylabel("Total Spent", fontsize=16)
        plt.title("Expense Trends Over Time (Category-wise)", fontsize=18)
        plt.xticks(rotation=45, fontsize=14)
        plt.legend(title="Categories", loc="upper left", fontsize=14)
        plt.grid(True)
        plt.savefig(trend_chart_path, bbox_inches="tight", dpi=300)
        plt.close()

        # Category-wise Spending Pie Chart (Full Page)
        pie_chart_path = f"expense_pie_chart_{user_id}.png"
        category_totals = df.groupby("category_name")["amount"].sum()
        plt.figure(figsize=(12, 12))  # ✅ Full Page Pie Chart
        plt.pie(category_totals, labels=category_totals.index, autopct="%1.1f%%", startangle=140)
        plt.title("Category-wise Spending", fontsize=18)
        plt.savefig(pie_chart_path, bbox_inches="tight", dpi=300)
        plt.close()

        # Total Spending by Category Bar Chart (Full Page)
        bar_chart_path = f"expense_bar_chart_{user_id}.png"
        plt.figure(figsize=(14, 10))  # ✅ Full Page Bar Chart
        plt.bar(category_totals.index, category_totals, color="blue")
        plt.xlabel("Category", fontsize=16)
        plt.ylabel("Total Spent", fontsize=16)
        plt.xticks(rotation=45, fontsize=14)
        plt.title("Total Spending by Category", fontsize=18)
        plt.savefig(bar_chart_path, bbox_inches="tight", dpi=300)
        plt.close()

        return trend_chart_path, pie_chart_path, bar_chart_path

    def generate_pdf_report(self, user_id):
        """Generate a detailed expense report in PDF format with full-page graphs."""
        df = self.fetch_expense_data(user_id)
        if df is None or df.empty:
            print("No expenses found to generate a report.")
            return
        
        # Generate Expense Graphs
        trend_chart, pie_chart, bar_chart = self.generate_expense_graphs(df, user_id)

        # Create PDF
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

        # Title
        self.set_font("Arial", "B", 18)
        self.cell(200, 15, f"Expense Report for User {user_id}", ln=True, align="C")
        self.ln(10)

        # Expense Table Header
        self.set_font("Arial", "B", 12)
        self.cell(30, 12, "Expense ID", 1)
        self.cell(50, 12, "Category", 1)
        self.cell(30, 12, "Amount", 1)
        self.cell(50, 12, "Description", 1)
        self.cell(30, 12, "Date", 1)
        self.ln()

        # Expense Table Data
        self.set_font("Arial", "", 11)
        for _, row in df.iterrows():
            self.cell(30, 12, str(row["id"]), 1)
            self.cell(50, 12, row["category_name"], 1)
            self.cell(30, 12, f"${row['amount']:.2f}", 1)
            self.cell(50, 12, row["description"], 1)
            self.cell(30, 12, row["date"].strftime('%Y-%m-%d'), 1)
            self.ln()

        # Add Full Page Charts
        if trend_chart:
            self.add_page()
            self.set_font("Arial", "B", 14)
            self.cell(200, 15, "Expense Trends Over Time", ln=True, align="C")
            self.ln(5)
            self.image(trend_chart, x=10, w=190)  # ✅ Full Page

        if pie_chart:
            self.add_page()
            self.set_font("Arial", "B", 14)
            self.cell(200, 15, "Category-wise Spending", ln=True, align="C")
            self.ln(5)
            self.image(pie_chart, x=10, w=190)  # ✅ Full Page

        if bar_chart:
            self.add_page()
            self.set_font("Arial", "B", 14)
            self.cell(200, 15, "Total Spending by Category", ln=True, align="C")
            self.ln(5)
            self.image(bar_chart, x=10, w=190)  # ✅ Full Page

        # Save PDF
        report_path = f"Expense_Report_User_{user_id}.pdf"
        self.output(report_path)
        log_user_action(user_id, f"Generated expense report: {report_path}")
        print(f"Expense report generated: {report_path}")
