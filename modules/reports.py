import streamlit as st
import pandas as pd

def show_reports():

    st.header("📄 Financial Reports")

    df = pd.read_csv(
        "data/sample_expense_data.csv"
    )

    st.download_button(
        label="Download CSV Report",
        data=df.to_csv(index=False),
        file_name="financial_report.csv",
        mime="text/csv"
    )

    st.dataframe(df.head(50))