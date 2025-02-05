import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="cashflow_compass",
            user="postgres",
            password="1806",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
