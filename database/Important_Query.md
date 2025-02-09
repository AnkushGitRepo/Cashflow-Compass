# Some important SELECT SQL queries you will frequently
- Use to fetch data for reports, analytics, and debugging.

### **📌 1️⃣ Retrieve All Users**
```sql
SELECT * FROM users;
```

### **📌 2️⃣ Retrieve a Specific User’s Details**
```sql
SELECT * FROM users WHERE username = 'testuser';
```

### **📌 3️⃣ Get All Categories for a User**
```sql
SELECT category_name FROM categories WHERE user_id = 5 OR user_id IS NULL;
```

### **📌 4️⃣ Fetch Expenses for a Specific User**
```sql
SELECT e.id, c.category_name, e.amount, e.description, e.date
FROM expenses e
JOIN categories c ON e.category_id = c.id
WHERE e.user_id = 5
ORDER BY e.date DESC;
```

### **📌 5️⃣ Fetch Last 30 Days' Spending (Category-wise)**
```sql
SELECT c.category_name, SUM(e.amount) AS total_spent
FROM expenses e
JOIN categories c ON e.category_id = c.id
WHERE e.user_id = 5 AND e.date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY c.category_name
ORDER BY total_spent DESC;
```

### **📌 6️⃣ Get Monthly Expenses for a User**
```sql
SELECT EXTRACT(MONTH FROM e.date) AS month, SUM(e.amount) AS total_spent
FROM expenses e
WHERE e.user_id = 5 AND EXTRACT(YEAR FROM e.date) = 2024
GROUP BY month
ORDER BY month;
```

### **📌 7️⃣ Get Yearly Expense Trends**
```sql
SELECT EXTRACT(YEAR FROM e.date) AS year, SUM(e.amount) AS total_spent
FROM expenses e
WHERE e.user_id = 5
GROUP BY year
ORDER BY year;
```

### **📌 8️⃣ Fetch Total Spending Per Category for a User**
```sql
SELECT c.category_name, SUM(e.amount) AS total_spent
FROM expenses e
JOIN categories c ON e.category_id = c.id
WHERE e.user_id = 5
GROUP BY c.category_name
ORDER BY total_spent DESC;
```

### **📌 9️⃣ Fetch All Expenses of a User Since Account Creation**
```sql
SELECT e.id, c.category_name, e.amount, e.description, e.date
FROM expenses e
JOIN categories c ON e.category_id = c.id
WHERE e.user_id = 5
ORDER BY e.date ASC;
```

### **📌 🔟 Fetch User Logs (Action History)**
```sql
SELECT * FROM user_logs WHERE user_id = 5 ORDER BY timestamp DESC;
```

