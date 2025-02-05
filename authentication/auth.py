import bcrypt
import getpass
import psycopg2
from config.db_config import get_db_connection

class Authentication:
    def __init__(self):
        self.conn = get_db_connection()

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

    # Add the signup method here
    def signup(self):
        """Sign up a new user and ensure unique usernames."""
        while True:
            username = input("\nEnter username: ").strip()
            
            if self.username_exists(username):
                print(f"Error: The username '{username}' is already taken. Please choose a different one.")
            else:
                break  # Username is unique, exit the loop

        password = getpass.getpass("Enter password: ")
        hashed_password = self.hash_password(password)

        try:
            with self.conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
                self.conn.commit()
                print("User registered successfully!")
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    
    # Add the login method here
    def login(self):
        username = input("\nEnter username: ")
        password = getpass.getpass("Enter password: ")

        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT password FROM users WHERE username = %s", (username,))
                user = cur.fetchone()

                if user and self.verify_password(password, user[0]):
                    print("Login successful!")
                    return True
                else:
                    print("Invalid username or password.")
                    return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def view_history(self):
        """Retrieve and display user action logs in a formatted table."""
        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT action, timestamp FROM user_logs ORDER BY timestamp DESC")
                logs = cur.fetchall()

                if not logs:
                    print("No user history found.")
                    return

                # Print table header
                print("\n--- User Action History ---\n")
                print(f"{'Description'.ljust(40)} | {'Timestamp'}")
                print("-" * 75)

                # Print each row dynamically formatted
                for action, timestamp in logs:
                    print(f"{action.ljust(40)} | {timestamp}")

                print("-" * 75)

        except Exception as e:
            print(f"Error retrieving user history: {e}")
