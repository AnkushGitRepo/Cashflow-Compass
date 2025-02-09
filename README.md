# 💰 CLI Expense Tracker [Cashflow Compass]

## 📌 Overview
The **CLI Expense Tracker** is a command-line-based expense management system that helps users track their daily, weekly, and monthly spending. Users can add, update, delete, and view expenses, generate reports, and visualize spending trends.

This project is built with **Python**, using **PostgreSQL** for data persistence, and **bcrypt** for secure password handling. It follows a **modular structure**, ensuring scalability and maintainability.

---

## 🚀 Features

- **User Authentication**: Secure signup & login with password hashing (bcrypt).
- **Expense Management**:
  - Add expenses with categories, descriptions, and date restrictions.
  - Delete expenses after searching by **category & date range**.
  - Update expenses with flexible field changes.
- **Category Management**:
  - View all categories in a **structured format**.
  - Create new categories.
  - Delete unused categories.
- **Reporting System**:
  - Generate daily, weekly, monthly, and yearly reports.
  - Compare expenses across different periods.
  - Export reports in PDF format.
- **Visualization & Graphs**:
  - **Pie charts**: Category-wise spending breakdown.
  - **Bar charts**: Monthly and yearly expense comparison.
  - **Line graphs**: Expense trends over time.
- **Logging & History**:
  - Track **all user actions** (expense updates, deletions, reports generated).
  - Maintain a history log of every action performed.

---

## 📂 Folder Structure
```
expense_tracker/
│── main.py
│── requirements.txt
|__ README.md
│
├── config/
│   ├── db_config.py
│
├── database/
│   ├── db_connection.py
│   ├── models.py
│
├── authentication/
│   ├── auth.py
│
├── expenses/
│   ├── expense_manager.py
│
├── categories/
│   ├── category_manager.py
│
├── reports/
│   ├── report_generator.py
│
├── utils/
│   ├── pdf_generator.py
│   ├── logger.py
```

---

## 🔧 Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/AnkushGitRepo/Cashflow-Compass.git
cd Cashflow-Compass
```

### **2️⃣ Create a Virtual Environment (`Recommended`)**
```
python -m venv .venv
source .venv/bin/activate  # For MacOS/Linux
.\.venv\Scripts\activate   # For Windows
```
### **3️⃣ Install Dependencies**
```
pip install -r requirements.txt
```

### **4️⃣ Set Up PostgreSQL Database**
- **1. Start PostgreSQL service:**
    ```
    sudo service postgresql start  # For Linux/macOS
    ```
- **2. Create a new database:**
    ```
    CREATE DATABASE expense_tracker;
    ```
- **3. Update Database Configuration in `config/db_config.py`:**
    ```python
    DB_NAME = "cashflow_compass"
    DB_USER = "postgres"
    DB_PASSWORD = "your_password"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    ```
### **5️⃣ Run the Database Migration**
```
python database/models.py
```
---
## ▶️ Running the Application
### Start the CLI Expense Tracker
```
python main.py
```

### User Menu
```mark
1. Signup
2. Login
3. Exit
Choose an option:
```

#### After login, users can:
```mark
1. Add Expense
2. Delete Expense
3. Update Expense
4. View Reports
5. Generate Reports
6. History
7. Categories
8. Exit
```
---
## 📘 Usage Guide
### **1️⃣ Adding an Expense**
- Users enter amount first.
- Categories are displayed in a formatted manner (6 per line).
- Date input:
    - Press Enter to use current date.
    - Can only enter dates within ±6 months.
- Logs are created in `user_logs` after expense addition.
### **2️⃣ Deleting an Expense**
- Users can search expenses before deleting:
    - By category.
    - By date range.
- Filtered expenses are displayed in a table before selection.
### **3️⃣ Updating an Expense**
- Users can search expenses before updating.
- Flexible updates:
    - Can skip fields (press Enter to keep old values).
    - Validates category & date input.
### **4️⃣ Viewing Reports**
- Users can generate reports:
    - Daily, Weekly, Monthly, and Yearly.
    - Comparison Reports (current vs. past months).
### **5️⃣ History & Logs**
- User logs track every action.
- Logs include:
    - Expense additions, updates, deletions.
    - Report generations.

---
## 🛠️ Database Schema
### 🗄 Users Table
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### 🗂 Categories Table
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_name VARCHAR(100) NOT NULL,
    is_predefined BOOLEAN DEFAULT FALSE
);
```
### 📊 Expenses Table
```sql
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
### 📜 User Logs Table
```sql
CREATE TABLE user_logs (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    action TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## ⚠️ Error Handling
- **Invalid Inputs:** Users are prompted again until valid data is entered.
- **Database Errors:** Issues are logged in `user_logs`.
- **Graceful Exits:** Users can cancel actions anytime.

## 🚀 Future Enhancements
- **📊 Advanced Analytics** (budgeting, spending trends).
- **📅 Recurring Expenses** (auto-add monthly subscriptions).
- **📱 Web Interface** (integrate with Flask or Django).
- **📤 Export to CSV/PDF** for detailed financial tracking.

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (feature-xyz).
3. Commit changes (git commit -m "Added feature XYZ").
4. Push and submit a PR.

## ✨ Acknowledgments
Special thanks to contributors for helping improve this project. 🚀

---

🚀 **Let me know if you need further refinements!** 🔥










