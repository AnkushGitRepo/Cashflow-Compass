import psycopg2
from config.db_config import get_db_connection
from datetime import datetime

def log_user_action(user_id, action):
    """Log user actions with a timestamp."""
    conn = get_db_connection()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO user_logs (user_id, action, timestamp) VALUES (%s, %s, %s)",
                (user_id, action, timestamp)
            )
            conn.commit()
    except Exception as e:
        print(f"Logging Error: {e}")
