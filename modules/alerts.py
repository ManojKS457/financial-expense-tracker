import streamlit as st
import pandas as pd

def show_alerts():

    st.header("🚨 Financial Alerts")

    df = pd.read_csv(
        "data/expense_data.csv",
        nrows=10000
    )

    total_amount = df["amount"].sum()

    monthly_budget = 5000000

    fraud_count = df["isFraud"].sum()

    st.metric(
        "Total Expenses",
        f"₹{total_amount:,.2f}"
    )

    st.metric(
        "Fraud Transactions",
        int(fraud_count)
    )

    if total_amount > monthly_budget:

        st.error(
            "Monthly budget exceeded!"
        )

    else:

        st.success(
            "Budget is within limit."
        )

    if fraud_count > 0:

        st.warning(
            f"{int(fraud_count)} fraud transactions detected."
        )