import streamlit as st
import pandas as pd

def show_reports():

    st.title("📄 Financial Reports")

    df = pd.read_csv("data/sample_expense_data.csv")

    st.subheader("Complete Expense Report")

    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download CSV Report",
        data=csv,
        file_name="financial_report.csv",
        mime="text/csv"
    )
