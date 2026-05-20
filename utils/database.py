import sqlite3

DB_PATH = "database/finance.db"

def create_connection():

    conn = sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

    return conn


def create_transactions_table():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            step INTEGER,
            type TEXT,
            amount REAL,
            sender TEXT,
            receiver TEXT
        )
    """)

    conn.commit()

    conn.close()