### **📌 Data Structures & Algorithms Used in Cashflow-Compass**  
**Cashflow Compass** project incorporates several **data structures and algorithms** for efficient data storage, retrieval, and processing. Below is a **detailed breakdown** of where and how **Data Structures & Algorithms** are used.

---

# **📌 Data Structures Used**

### **1️⃣ Lists (`list`)**
📍 **Where Used?**  
- **Displaying categories (6 per line)**
- **Fetching user-created categories before deletion**
- **Handling search results for expenses**  

📍 **How Used?**
- When **viewing categories**, a `list` is used to **store and format categories** efficiently.
- In **expense searching**, expenses are fetched into a list before filtering.
- The **user-created categories** list ensures that users **can only delete their own categories**.

📌 **Example: Displaying Categories (6 per line)**
```python
categories = ["Food", "Rent", "Utilities", "Transportation", "Entertainment", "Medical", "Gym"]
for i in range(0, len(categories), 6):
    print("   ".join(f"{cat:<15}" for cat in categories[i:i+6]))  
```
✅ **Time Complexity:** **O(N)** (Iterates once over the categories).  
✅ **Space Complexity:** **O(N)** (Stores all categories in memory).

---

### **2️⃣ Dictionaries (`dict`)**
📍 **Where Used?**  
- **Storing logged-in user details (`current_user`)**
- **Mapping category names to category IDs**
- **Caching user credentials during login to prevent redundant queries**

📍 **How Used?**
- **`current_user = {}`** stores `id` and `username`, avoiding multiple DB queries.
- When **mapping category names to IDs**, a dictionary ensures **O(1) retrieval**.

📌 **Example: Storing Logged-in User Details**
```python
self.current_user = {"id": user[0], "username": user[1]}
```
✅ **Time Complexity:** **O(1)** (Constant time retrieval).  
✅ **Space Complexity:** **O(1)** (Stores only a single user session).

---

### **3️⃣ Sets (`set`)**
📍 **Where Used?**  
- **Ensuring unique category names when displayed**
- **Checking if a category already exists before creation**
- **Handling unique expenses when filtering reports**

📍 **How Used?**
- A **set ensures no duplicate categories** when displaying them.
- Before inserting a category, it checks against a **set of existing categories**.

📌 **Example: Preventing Duplicate Categories**
```python
existing_categories = {cat[0] for cat in categories}  # Convert fetched categories to a set
if category_name in existing_categories:
    print("⚠️ This category already exists!")
```
✅ **Time Complexity:** **O(1)** (Set lookup is constant time).  
✅ **Space Complexity:** **O(N)** (Stores categories in memory).

---

# **📌 Algorithms Used**

### **1️⃣ Binary Search (`O(log N)`)**
📍 **Where Used?**  
- **Searching expenses by date range**
- **Finding an expense ID before updating or deleting it**

📍 **How Used?**
- When **searching for an expense**, instead of scanning **all records (`O(N)`)**, we sort them by date and apply **Binary Search (`O(log N)`)**.

📌 **Example: Searching an Expense by Date**
```python
expenses.sort(key=lambda x: x['date'])  # Sort expenses by date (O(N log N))
low, high = 0, len(expenses) - 1
target_date = "2025-02-10"

while low <= high:
    mid = (low + high) // 2
    if expenses[mid]['date'] == target_date:
        print("Expense Found:", expenses[mid])
        break
    elif expenses[mid]['date'] < target_date:
        low = mid + 1
    else:
        high = mid - 1
```
✅ **Time Complexity:** **O(log N)** (Binary search is logarithmic).  
✅ **Space Complexity:** **O(1)** (No extra space used).

---

### **2️⃣ Sorting Algorithms (`O(N log N)`)**
📍 **Where Used?**  
- **Sorting expenses by date**
- **Sorting spending categories in reports (highest to lowest spending)**

📍 **How Used?**
- **`sorted()` in Python uses Timsort (`O(N log N)`)**, which is optimized for real-world data.

📌 **Example: Sorting Expenses by Amount**
```python
sorted_expenses = sorted(expenses, key=lambda x: x['amount'], reverse=True)
```
✅ **Time Complexity:** **O(N log N)** (Timsort is efficient).  
✅ **Space Complexity:** **O(N)** (Stores a sorted copy).

---

### **3️⃣ Hashing (`O(1)`)**
📍 **Where Used?**  
- **Storing user passwords securely (`bcrypt.hashpw()`)**
- **Caching previously fetched database queries (e.g., login session caching)**

📍 **How Used?**
- **User passwords are hashed** before storing them in the database.

📌 **Example: Hashing a Password (`bcrypt`)**
```python
import bcrypt

password = "SecurePass@123"
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```
✅ **Time Complexity:** **O(1)** (Hashing is constant time).  
✅ **Space Complexity:** **O(1)** (Stores hashed password as a fixed-length string).

---

### **4️⃣ Greedy Algorithm (`O(N)`)**
📍 **Where Used?**  
- **Generating financial reports (aggregating expenses category-wise)**
- **Finding the top 3 spending categories quickly**

📍 **How Used?**
- **Aggregates category-wise spending** in a single pass (`O(N)`).

📌 **Example: Finding the Top 3 Spending Categories**
```python
top_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)[:3]
```
✅ **Time Complexity:** **O(N log N)** (Sorting takes `O(N log N)`, slicing takes `O(1)`).  
✅ **Space Complexity:** **O(N)** (Stores category spending data).

---

# **📌 Summary Table: Data Structures & Algorithms Used**
| **Concept**  | **Where Used?** | **Time Complexity** | **Space Complexity** |
|-------------|---------------|------------------|------------------|
| **List (`list`)** | Displaying categories (6 per line), Storing search results | **O(N)** | **O(N)** |
| **Dictionary (`dict`)** | Storing logged-in user, Mapping category names to IDs | **O(1)** | **O(1)** |
| **Set (`set`)** | Ensuring unique category names, Preventing duplicates | **O(1)** | **O(N)** |
| **Binary Search (`O(log N)`)** | Searching expenses by date | **O(log N)** | **O(1)** |
| **Sorting (`O(N log N)`)** | Sorting expenses, Finding highest spending categories | **O(N log N)** | **O(N)** |
| **Hashing (`bcrypt`)** | Storing user passwords securely | **O(1)** | **O(1)** |
| **Greedy Algorithm (`O(N)`)** | Finding top 3 spending categories | **O(N log N)** | **O(N)** |

---

# **✅ Conclusion**
Your **CLI Expense Tracker** efficiently uses **various data structures and algorithms** to:
- **Optimize searches** (`Binary Search`)
- **Ensure security** (`Hashing for passwords`)
- **Enhance performance** (`Sorting, Hashing, Greedy Algorithm`)
- **Improve usability** (`Lists, Dictionaries, Sets`)

🚀 **Now, You Have a Deep Understanding of How Data Structures & Algorithms Are Used in Your Project!**  
Let me know if you need further clarifications! 🔥