import streamlit as st
import pandas as pd

def show_dashboard():

    st.title("💰 AI Financial Analytics Dashboard")

    st.markdown("""
    Real-Time Banking Transaction Intelligence System
    """)

    df = pd.read_csv(
        "data/expense_data.csv",
        nrows=10000
    )

    total_amount = df["amount"].sum()

    average_amount = df["amount"].mean()

    highest_transaction = df["amount"].max()

    fraud_transactions = df["isFraud"].sum()

    monthly_budget = 5000000

    remaining_budget = monthly_budget - total_amount

    budget_usage = int(
        (total_amount / monthly_budget) * 100
    )

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💸 Total Expenses",
        f"₹{total_amount:,.2f}"
    )

    col2.metric(
        "📊 Average Transaction",
        f"₹{average_amount:,.2f}"
    )

    col3.metric(
        "🔥 Highest Transaction",
        f"₹{highest_transaction:,.2f}"
    )

    col4.metric(
        "🚨 Fraud Transactions",
        int(fraud_transactions)
    )

    st.markdown("---")

    # Budget Analysis
    st.subheader("💵 Monthly Budget Analysis")

    col5, col6 = st.columns(2)

    col5.metric(
        "Monthly Budget",
        f"₹{monthly_budget:,.2f}"
    )

    col6.metric(
        "Remaining Budget",
        f"₹{remaining_budget:,.2f}"
    )

    st.progress(min(budget_usage, 100))

    st.write(f"Budget Usage: {budget_usage}%")

    st.markdown("---")

    # AI Insights
    st.subheader("🤖 AI Insights")

    if fraud_transactions > 0:

        st.warning(
            "High-risk fraud transactions detected."
        )

    if average_amount > 50000:

        st.info(
            "Average transaction amount is unusually high."
        )

    if total_amount > monthly_budget:

        st.error(
            "Monthly budget exceeded."
        )

    else:

        st.success(
            "Expenses are within monthly budget."
        )

    st.markdown("---")

    st.subheader("📄 Recent Transactions")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )