# **📄 Expense Tracker - Complete Documentation**

## **📌 Overview**
The **CLI Expense Tracker** is a command-line-based financial management system that helps users **track, categorize, analyze, and visualize** their expenses. It supports **daily, weekly, monthly, and yearly expense tracking**, along with advanced reporting and graphical analysis.

This documentation provides a **detailed explanation** of the project, including:
- **System Flow** (Method Call Structure)
- **Database Schema**
- **Feature Breakdown**
- **Folder Structure**
- **Setup & Installation**
- **Usage Guide**
- **Common SQL Queries**

---

# **📌 System Flow (Method Call Structure)**
This section provides a **step-by-step breakdown** of **which method calls which method** and how they interact.

---

## **1️⃣ Home Menu (main.py)**
### 📌 **Method Calls**
- **`home_options()`** → Displays **Signup, Login, Exit** options.
- **If Signup (`auth.signup()`)** → Calls `auth.signup()`, then `auth.login()`, then `users_logged_in()`.
- **If Login (`auth.login()`)** → Calls `auth.login()`, then `users_logged_in()`.
- **If Exit** → Calls `display_goodbye()` and exits.

### 📌 **Flow Diagram**
```plaintext
main.py
 ├── home_options()
     ├── auth.signup()  → If successful, calls auth.login()
     │   ├── If successful, calls users_logged_in()
     ├── auth.login()  → Calls users_logged_in()
     ├── display_goodbye()  → Exits the application
```

---

## **2️⃣ Signup & Login (auth.py)**
### 📌 **Method Calls**
- **Signup (`auth.signup()`)**
  - Checks if **username is valid**.
  - **Validates password strength**.
  - Inserts **user into the database**.
  - Calls `auth.login()` immediately after successful signup.

- **Login (`auth.login()`)**
  - If user is **already logged in**, it skips re-authentication.
  - **Verifies credentials**, then stores session.

### 📌 **Flow Diagram**
```plaintext
auth.signup()
 ├── Validates username
 ├── Validates password strength
 ├── Stores user in database
 ├── Calls auth.login()  → Directly logs in new user

auth.login()
 ├── Checks if user is already logged in
 ├── Verifies credentials
 ├── Stores session
 ├── Returns user_id
```

---

## **3️⃣ Users Logged In (`users_logged_in()`)**
### 📌 **Method Calls**
- Calls **expense, category, history, and report functionalities** based on user choice.

### 📌 **Flow Diagram**
```plaintext
users_logged_in(user_id)
 ├── Calls expense_manager.add_expense()
 ├── Calls expense_manager.delete_expense()
 ├── Calls expense_manager.update_expense()
 ├── Calls report_generator.view_reports()
 ├── Calls report_generator.generate_pdf_report()
 ├── Calls auth.view_history()
 ├── Calls category_manager.manage_categories()
 ├── Calls home_options() on exit
```

---

## **4️⃣ Expense Management (`expense_manager.py`)**
### 📌 **Method Calls**
- **Add Expense (`expense_manager.add_expense()`)**
  - Displays **categories (6 per line)**.
  - **Ensures input validation (date range, amount)**.
  - **Logs the action** in `user_logs`.

- **Delete Expense (`expense_manager.delete_expense()`)**
  - Allows filtering **expenses by category/date**.
  - Displays **filtered expenses in a table**.
  - **Deletes selected expense** and logs the action.

- **Update Expense (`expense_manager.update_expense()`)**
  - Allows filtering **expenses by category/date**.
  - Displays **filtered expenses in a table**.
  - **Allows selective updates (amount, date, description)**.
  - **Logs the action** in `user_logs`.

### 📌 **Flow Diagram**
```plaintext
expense_manager.add_expense()
 ├── Shows categories (6 per line)
 ├── Takes valid input (date range, amount)
 ├── Inserts expense into DB
 ├── Logs action in user_logs

expense_manager.delete_expense()
 ├── Filters expenses by category/date
 ├── Displays expenses in a table
 ├── Deletes selected expense
 ├── Logs action in user_logs

expense_manager.update_expense()
 ├── Filters expenses by category/date
 ├── Displays expenses in a table
 ├── Allows selective updates
 ├── Logs action in user_logs
```

---

## **5️⃣ Category Management (`category_manager.py`)**
### 📌 **Method Calls**
- **View Categories (`category_manager.display_categories()`)**
  - Displays categories **6 per line**.
  - **Ensures deleted categories do not appear**.

- **View Last 30 Days' Spending (`category_manager.show_spending_last_30_days()`)**
  - Displays **category-wise total spending in a table**.
  - **Includes total spending row**.

- **Create New Category (`category_manager.create_category()`)**
  - **Prevents duplicate category creation**.
  - **Capitalizes first letter**.
  - Inserts **new category into DB**.

- **Delete Category (`category_manager.delete_category()`)**
  - Displays **only user-created categories**.
  - **Prevents deletion of predefined categories**.
  - **Deletes associated expenses**.
  - **Logs action in `user_logs`**.

---

## **6️⃣ Reports & Graphs (`report_generator.py`)**
### 📌 **Method Calls**
- **View Reports (`report_generator.view_reports()`)**
  - Calls:
    - `generate_daily_report()`
    - `generate_weekly_report()`
    - `generate_monthly_report()`
    - `generate_yearly_report()`
    - `generate_comparison_report()`

- **Generate PDF Reports (`pdf_generator.py`)**
  - **Expense Table**
  - **Expense Trend Graph**
  - **Pie Chart**
  - **Bar Chart**
  - **Category-wise summary table**

---

## **FLow Chart**
<img title="Flow of Program" alt="Alt text" src="/docs/flow.png">
![Flow of Program](https://github.com/AnkushGitRepo/Cashflow-Compass/blob/main/docs/flow.png "Flow of Program")

# **📌 Database Schema**
### **Users Table**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Categories Table**
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_name VARCHAR(100) NOT NULL,
    is_predefined BOOLEAN DEFAULT FALSE
);
```

### **Expenses Table**
```sql
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT,
    date DATE NOT NULL
);
```

### **User Logs Table**
```sql
CREATE TABLE user_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    action TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---
