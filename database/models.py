import psycopg2
from config.db_config import get_db_connection

def create_tables():
    """Creates tables for the expense tracker application."""
    conn = get_db_connection()
    if conn is None:
        print("Error: Could not connect to the database.")
        return

    try:
        with conn.cursor() as cur:
            # Users Table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # Categories Table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(id) ON DELETE CASCADE,
                    category_name VARCHAR(100) NOT NULL,
                    is_predefined BOOLEAN DEFAULT FALSE,
                    UNIQUE (user_id, category_name)
                );
            """)

            # Expenses Table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(id) ON DELETE CASCADE,
                    category_id INT REFERENCES categories(id) ON DELETE SET NULL,
                    amount DECIMAL(10,2) NOT NULL,
                    description TEXT DEFAULT '',
                    date DATE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # User Logs Table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_logs (
                    id SERIAL PRIMARY KEY,
                    user_id INT REFERENCES users(id) ON DELETE CASCADE,
                    action TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            conn.commit()
            print("✅ Tables created successfully!")

    except Exception as e:
        print(f"❌ Error creating tables: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_tables()
