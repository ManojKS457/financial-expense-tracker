import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("📊 Financial Analytics")

    df = pd.read_csv(
        "data/sample_expense_data.csv"
    )

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ---------------- PIE CHART ---------------- #

    st.subheader("Transaction Types")

    type_data = (
        df.groupby("type")["amount"]
        .sum()
        .reset_index()
    )

    fig1 = px.pie(
        type_data,
        names="type",
        values="amount",
        title="Transaction Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ---------------- BAR CHART ---------------- #

    st.subheader("Top Transactions")

    top_data = (
        df.sort_values(
            by="amount",
            ascending=False
        )
        .head(15)
    )

    fig2 = px.bar(
        top_data,
        x="nameOrig",
        y="amount",
        color="type",
        title="Highest Transactions"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ---------------- FRAUD ANALYSIS ---------------- #

    st.subheader("Fraud Transactions")

    fraud_data = (
        df["isFraud"]
        .value_counts()
        .reset_index()
    )

    fraud_data.columns = [
        "Fraud",
        "Count"
    ]

    fig3 = px.bar(
        fraud_data,
        x="Fraud",
        y="Count",
        title="Fraud Detection Analysis"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )
