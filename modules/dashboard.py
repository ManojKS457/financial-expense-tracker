import streamlit as st
import pandas as pd

def show_dashboard():

    st.title("💰 AI Financial Analytics Dashboard")

    df = pd.read_csv("data/sample_expense_data.csv")

    total_expense = df["amount"].sum()

    avg_expense = df["amount"].mean()

    highest_expense = df["amount"].max()

    fraud_count = len(df[df["isFraud"] == 1])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Expenses", f"₹{total_expense:,.2f}")

    col2.metric("Average Expense", f"₹{avg_expense:,.2f}")

    col3.metric("Highest Expense", f"₹{highest_expense:,.2f}")

    col4.metric("Fraud Transactions", fraud_count)

    st.divider()

    st.subheader("Recent Transactions")

    st.dataframe(df.head(10))
