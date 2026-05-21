import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("📊 Financial Analytics Dashboard")

    # LOAD DATA

    df = pd.read_csv("data/sample_expense_data.csv")

    # DATA PREVIEW

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ---------------- TOTALS ---------------- #

    total_amount = df["amount"].sum()

    fraud_count = df["isFraud"].sum()

    avg_amount = df["amount"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", f"₹ {total_amount:,.2f}")

    col2.metric("Fraud Transactions", int(fraud_count))

    col3.metric("Average Amount", f"₹ {avg_amount:,.2f}")

    # ---------------- BAR CHART ---------------- #

    st.subheader("Transaction Type Analysis")

    type_data = (
        df.groupby("type")["amount"]
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        type_data,
        x="type",
        y="amount",
        color="type",
        title="Total Amount by Transaction Type"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ---------------- PIE CHART ---------------- #

    st.subheader("Fraud vs Legitimate Transactions")

    fraud_data = df["isFraud"].value_counts().reset_index()

    fraud_data.columns = ["Fraud", "Count"]

    fraud_data["Fraud"] = fraud_data["Fraud"].replace({
        0: "Legitimate",
        1: "Fraud"
    })

    fig2 = px.pie(
        fraud_data,
        names="Fraud",
        values="Count",
        title="Fraud Detection Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ---------------- TOP TRANSACTIONS ---------------- #

    st.subheader("Top 10 Highest Transactions")

    top_transactions = (
        df.sort_values(
            by="amount",
            ascending=False
        )
        .head(10)
    )

    fig3 = px.bar(
        top_transactions,
        x="nameOrig",
        y="amount",
        color="type",
        title="Top Transactions"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
