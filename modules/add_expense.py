import streamlit as st
import sqlite3

def show_add_expense():

    st.header("➕ Add Transaction")

    step = st.number_input("Step")

    transaction_type = st.selectbox(
        "Transaction Type",
        [
            "PAYMENT",
            "TRANSFER",
            "DEBIT",
            "CASH_OUT"
        ]
    )

    amount = st.number_input("Amount")

    sender = st.text_input("Sender")

    receiver = st.text_input("Receiver")

    if st.button("Add Transaction"):

        conn = sqlite3.connect(
            "database/finance.db"
        )

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

        cursor.execute("""
            INSERT INTO transactions
            (
                step,
                type,
                amount,
                sender,
                receiver
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            step,
            transaction_type,
            amount,
            sender,
            receiver
        ))

        conn.commit()

        conn.close()

        st.success(
            "Transaction added successfully!"
        )