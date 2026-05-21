import streamlit as st
import pandas as pd
import plotly.express as px

def show_analytics():

    st.title("📊 Expense Analytics")

    df = pd.read_csv("data/sample_expense_data.csv")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # CATEGORY ANALYSIS

    category_data = (
        df.groupby("type")["amount"]
        .sum()
        .reset_index()
    )

    fig1 = px.pie(
        category_data,
        names="type",
        values="amount",
        title="Expense Distribution"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # BAR CHART

    fig2 = px.bar(
        df.head(20),
        x="step",
        y="amount",
        color="type",
        title="Transaction Amount Analysis"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # LINE CHART

    fig3 = px.line(
        df.head(50),
        x="step",
        y="amount",
        title="Expense Trend"
    )

    st.plotly_chart(fig3, use_container_width=True)
