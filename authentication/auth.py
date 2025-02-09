import bcrypt
import getpass
import re
import psycopg2
from config.db_config import get_db_connection

class Authentication:
    def __init__(self):
        self.conn = get_db_connection()
        self.current_user = None

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def verify_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    # Add the username_exists method here
    def username_exists(self, username):
        """Check if the username already exists in the database."""
        with self.conn.cursor() as cur:
            cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
            return cur.fetchone() is not None

    def username_exists(self, username):
        """Check if the username already exists in the database."""
        with self.conn.cursor() as cur:
            cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
            return cur.fetchone() is not None

    def is_strong_password(self, password):
        """Check if the password meets strength requirements."""
        if (len(password) >= 8 and 
            re.search(r"[A-Z]", password) and 
            re.search(r"[a-z]", password) and 
            re.search(r"\d", password) and 
            re.search(r"[!@#$%^&*]", password)):
            return True
        return False

    def signup(self):
        """Sign up a new user with a strong password and return to home menu if canceled."""
        while True:
            username = input("\nEnter username (or type 'cancel' to return to the home menu): ").strip()

            if not username:
                print("⚠️ Username cannot be empty. Please enter a valid username.")
                continue

            if username.lower() == "cancel":
                print("❌ Signup process canceled. Returning to home menu...")
                return None  # ✅ Return to home menu

            if self.username_exists(username):
                print(f"⚠️ The username '{username}' is already taken. Please choose a different one.")
            else:
                break

        while True:
            password = getpass.getpass("Enter a strong password (Min 8 chars, 1 Uppercase, 1 Lowercase, 1 Number, 1 Special char): ")

            if self.is_strong_password(password):
                break
            else:
                print("⚠️ Weak password! Ensure it has at least 8 characters, one uppercase, one lowercase, one digit, and one special character.")

        hashed_password = self.hash_password(password)

        try:
            with self.conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id", 
                            (username, hashed_password))
                user_id = cur.fetchone()[0]
                self.conn.commit()
                print("✅ User registered successfully!")

                # ✅ Update session with new user
                self.current_user = {"id": user_id, "username": username}  
                print(f"✅ You are now logged in as '{username}'!")
                return user_id  # ✅ Return the correct user_id
        except Exception as e:
            print(f"⚠️ Error: {e}")
            return None

    def login(self, username=None):
        """Login user and prevent repeated login prompts."""
        if self.current_user:  # ✅ Prevents re-entering credentials
            print(f"✅ You are already logged in as '{self.current_user['username']}'!")
            return self.current_user['id']

        if not username:
            username = input("\nEnter username (or type 'cancel' to return to the home menu): ").strip()

        if username.lower() == "cancel":
            print("❌ Login process canceled. Returning to home menu...")
            return None  # ✅ Return to home menu

        password = getpass.getpass("Enter password: ")

        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT id, username, password FROM users WHERE username = %s", (username,))
                user = cur.fetchone()

                if user and self.verify_password(password, user[2]):
                    print("✅ Login successful!")
                    self.current_user = {"id": user[0], "username": user[1]}  # ✅ Correctly update current_user
                    return user[0]
                else:
                    print("⚠️ Invalid username or password.")
                    return None
        except Exception as e:
            print(f"⚠️ Error: {e}")
            return None

        
    def view_history(self,user_id):
        """Retrieve and display user action logs in a formatted table."""
        try:
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT action, timestamp FROM user_logs where user_id = '{user_id}' ORDER BY timestamp DESC")
                logs = cur.fetchall()

                if not logs:
                    print("No user history found.")
                    return

                # Print table header
                print("\n--- User Action History ---\n")
                print(f"{'Description'.ljust(70)} | {'Timestamp'}")
                print("-" * 95)

                # Print each row dynamically formatted
                for action, timestamp in logs:
                    print(f"{action.ljust(70)} | {timestamp}")

                print("-" * 95)

        except Exception as e:
            print(f"Error retrieving user history: {e}")
