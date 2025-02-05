from pyfiglet import figlet_format
from termcolor import colored
from authentication.auth import Authentication
from categories.category_manager import CategoryManager
from expenses.expense_manager import ExpenseManager
from reports.report_generator import ReportGenerator

def main():
    auth = Authentication()
    expense_manager = ExpenseManager()
    report_generator = ReportGenerator()
    category_manager = CategoryManager()

    def display_welcome():
        welcome_text = figlet_format("Cashflow Compass", font="smslant") # Try fonts like "standard", "big", or "smslant"
        colored_text = colored(welcome_text, "magenta")  # Change to any color: red, green, yellow, blue
        print(colored_text)

    def display_goodbye():
        goodbye_text = figlet_format("Goodbye!", font="smslant")
        colored_text = colored(goodbye_text, "magenta")
        print(colored_text)

    def get_valid_choice():
        """Keep asking the user until they enter a valid choice (1, 2, or 3)."""
        valid_choices = {"1", "2", "3"}
        
        while True:
            choice = input("Choose an option: ").strip()
            if choice in valid_choices:
                return choice
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Function to handle user interactions after logging in
    def users_logged_in():
        while True:
            print("\n1. Add Expense\n2. Delete Expense\n3. Update Expense\n4. View Reports\n5. Generate Reports\n6. History\n7. Categories\n8. Exit")
            option = input("Choose an option: ")

            if option == "1":
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")
                date = input("Enter date (YYYY-MM-DD): ")
                expense_manager.add_expense(amount, category, description, date)
            elif option == "2":
                expense_id = int(input("Enter expense ID to delete: "))
                expense_manager.delete_expense(expense_id)
            elif option == "3":
                expense_id = int(input("Enter expense ID to update: "))
                new_amount = float(input("Enter new amount: "))
                new_category = input("Enter new category: ")
                new_description = input("Enter new description: ")
                new_date = input("Enter new date (YYYY-MM-DD): ")
                expense_manager.update_expense(expense_id, new_amount, new_category, new_description, new_date)
            elif option == "4":
                month = int(input("Enter month: "))
                year = int(input("Enter year: "))
                report_generator.view_reports(month, year)
            elif option == "5":
                report_generator.generate_report()
            elif option == "6":
                auth.view_history()
            elif option == "7":
                category_manager.manage_categories()  # ✅ New function for category management
            elif option == "8":
                home_options()
                break
            else:
                print("Invalid option.")


    # Function to display home options
    def home_options():
        options = print("\n1. Signup\n2. Login\n3. Exit")
        choice = get_valid_choice()
        
        if choice == "1":
            if auth.signup():
                users_logged_in()
        elif choice == "2":
            if auth.login():
                users_logged_in()
        elif choice == "3":
            display_goodbye()
        else:
            print("Invalid choice.")

    # Main program starts here
    display_welcome()
    home_options()

if __name__ == "__main__":
    main()
