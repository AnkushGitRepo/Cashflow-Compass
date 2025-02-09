from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
from datetime import datetime, timedelta
import numpy as np
from config.db_config import get_db_connection
from utils.logger import log_user_action

class PDFGenerator(FPDF):
    """Class to generate detailed PDF reports of expenses."""

    def __init__(self):
        super().__init__()
        self.conn = get_db_connection()

    def fetch_expense_data(self, user_id, months=6):
        """Fetch all expense data for the given user over the last `months` months."""
        query = """
            SELECT e.id, c.category_name, e.amount, e.description, e.date, u.username
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            JOIN users u ON e.user_id = u.id
            WHERE e.user_id = %s
            ORDER BY e.date ASC;
        """
        try:
            return pd.read_sql(query, self.conn, params=(user_id,))
        except Exception as e:
            print(f"Error fetching expense data: {e}")
            return None

    def generate_expense_graphs(self, df, user_id):
        """Generate and save expense trend graph, category-wise donut chart, and summary table."""
        if df.empty:
            return None, None, None
        
        df["date"] = pd.to_datetime(df["date"])
        df["year"] = df["date"].dt.year

        # Limit to last 5 years
        latest_year = df["year"].max()
        earliest_year = latest_year - 4  # Last 5 years
        df = df[df["year"] >= earliest_year]

        # Expense Trend Over the Past 5 Years (Line Chart)
        trend_chart_path = f"expense_trend_chart_{user_id}.png"
        yearly_df = df.groupby("year")["amount"].sum()
        plt.figure(figsize=(10, 5))
        plt.plot(yearly_df.index, yearly_df.values, marker="o", linestyle="--", color="b")
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Total Spent", fontsize=14)
        plt.title("Expense Trend Over the Past 5 Years", fontsize=16)
        plt.grid(True)
        plt.savefig(trend_chart_path, bbox_inches="tight", dpi=300)
        plt.close()

        # Category-Wise Spending Over the Past 6 Months (Donut Chart with Legend)
        pie_chart_path = f"expense_pie_chart_{user_id}.png"
        category_totals = df.groupby("category_name")["amount"].sum()
        plt.figure(figsize=(8, 8))
        wedges, texts, autotexts = plt.pie(
            category_totals, labels=category_totals.index, autopct="%1.1f%%",
            startangle=140, wedgeprops={"edgecolor": "white"}
        )
        for text in texts + autotexts:
            text.set_fontsize(12)  # Improve text visibility
        plt.legend(title="Categories", loc="best", fontsize=12)
        plt.title("Category Wise Spending Over The Years", fontsize=16)
        plt.savefig(pie_chart_path, bbox_inches="tight", dpi=300)
        plt.close()

        # Total Spending by Category Bar Chart (Colored Bars & Grid)
        bar_chart_path = f"expense_bar_chart_{user_id}.png"
        colors = plt.cm.viridis(np.linspace(0, 1, len(category_totals)))  # Generate different colors
        plt.figure(figsize=(10, 6))
        plt.bar(category_totals.index, category_totals, color=colors)
        plt.xlabel("Category", fontsize=14)
        plt.ylabel("Total Spent", fontsize=14)
        plt.xticks(rotation=45, fontsize=12)
        plt.title("Total Spending by Category", fontsize=16)
        plt.grid(axis="y", linestyle="--", alpha=0.7)  # Add a grid for readability
        plt.savefig(bar_chart_path, bbox_inches="tight", dpi=300)
        plt.close()

        return trend_chart_path, pie_chart_path, bar_chart_path

    def generate_pdf_report(self, user_id):
        """Generate a detailed expense report in PDF format."""
        df = self.fetch_expense_data(user_id)
        if df is None or df.empty:
            print("No expenses found to generate a report.")
            return

        username = df["username"].iloc[0]  # Get username from the dataset

        # Generate Expense Graphs
        trend_chart, pie_chart, bar_chart = self.generate_expense_graphs(df, user_id)

        # Create PDF
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()

        # Title with Username
        self.set_font("Arial", "B", 18)
        self.cell(200, 15, f"Expense Report for {username}", ln=True, align="C")
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
            self.cell(200, 15, "Expense Trend Over the Past 5 Years", ln=True, align="C")
            self.image(trend_chart, x=10, w=190)  

        if pie_chart:
            self.add_page()
            self.cell(200, 15, "Category Wise Spending Over The Years", ln=True, align="C")
            self.image(pie_chart, x=10, w=190)  

        if bar_chart:
            self.add_page()
            self.cell(200, 15, "Total Spending by Category", ln=True, align="C")
            self.image(bar_chart, x=10, w=190)  

        # Save PDF
        report_path = f"Expense_Report_{username}.pdf"
        self.output(report_path)
        log_user_action(user_id, f"Generated expense report: {report_path}")
        print(f"Expense report generated: {report_path}")
