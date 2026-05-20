import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("📈 Financial Analytics")

    df = pd.read_csv(
        "data/sample_expense_data.csv"
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Transaction Analysis",
            "Fraud Analysis",
            "Spending Patterns"
        ]
    )

    with tab1:

        st.subheader("Transaction Distribution")

        type_data = (
            df.groupby("type")["amount"]
            .sum()
            .reset_index()
        )

        fig1 = px.pie(
            type_data,
            names="type",
            values="amount",
            hole=0.4,
            title="Transaction Distribution"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

        fig2 = px.bar(
            type_data,
            x="type",
            y="amount",
            title="Transaction Comparison"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with tab2:

        st.subheader("Fraud Detection Analysis")

        fraud_data = (
            df.groupby("isFraud")
            .size()
            .reset_index(name="count")
        )

        fig3 = px.bar(
            fraud_data,
            x="isFraud",
            y="count",
            title="Fraud vs Non-Fraud"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with tab3:

        st.subheader("Spending Pattern Trends")

        trend_data = (
            df.groupby("step")["amount"]
            .sum()
            .reset_index()
        )

        fig4 = px.line(
            trend_data,
            x="step",
            y="amount",
            title="Transaction Trend"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )