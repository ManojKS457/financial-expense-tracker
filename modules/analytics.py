import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("📊 Financial Analytics Dashboard")

    # LOAD DATA

    df = pd.read_csv("data/sample_expense_data.csv")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # METRICS

    total_amount = df["amount"].sum()
    fraud_count = df["isFraud"].sum()
    avg_amount = df["amount"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Transactions",
        f"₹ {total_amount:,.2f}"
    )

    col2.metric(
        "Fraud Transactions",
        int(fraud_count)
    )

    col3.metric(
        "Average Amount",
        f"₹ {avg_amount:,.2f}"
    )

    # ================= LINE GRAPH =================

    st.subheader("📈 Expense Trend Over Steps")

    trend_data = (
        df.groupby("step")["amount"]
        .sum()
        .reset_index()
    )

    fig_line = px.line(
        trend_data,
        x="step",
        y="amount",
        markers=True,
        title="Expense Trend"
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )

    # ================= BAR GRAPH =================

    st.subheader("📊 Transaction Type Analysis")

    type_data = (
        df.groupby("type")["amount"]
        .sum()
        .reset_index()
    )

    fig_bar = px.bar(
        type_data,
        x="type",
        y="amount",
        color="type",
        title="Total Amount by Transaction Type"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

    # ================= PIE CHART =================

    st.subheader("🥧 Fraud Detection Distribution")

    fraud_data = (
        df["isFraud"]
        .value_counts()
        .reset_index()
    )

    fraud_data.columns = ["Fraud", "Count"]

    fraud_data["Fraud"] = fraud_data["Fraud"].replace({
        0: "Legitimate",
        1: "Fraud"
    })

    fig_pie = px.pie(
        fraud_data,
        names="Fraud",
        values="Count",
        title="Fraud vs Legitimate Transactions"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    # ================= TOP TRANSACTIONS =================

    st.subheader("💰 Top 10 Highest Transactions")

    top_transactions = (
        df.sort_values(
            by="amount",
            ascending=False
        )
        .head(10)
    )

    fig_top = px.bar(
        top_transactions,
        x="nameOrig",
        y="amount",
        color="type",
        title="Top Transactions"
    )

    st.plotly_chart(
        fig_top,
        use_container_width=True
    )
