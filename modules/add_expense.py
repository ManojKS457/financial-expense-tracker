import streamlit as st

def show_add_expense():

    st.title("➕ Add Expense")

    with st.form("expense_form"):

        expense_type = st.selectbox(
            "Expense Type",
            [
                "PAYMENT",
                "TRANSFER",
                "CASH_OUT",
                "DEBIT"
            ]
        )

        amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=100.0
        )

        sender = st.text_input("Sender Name")

        receiver = st.text_input("Receiver Name")

        submit = st.form_submit_button("Add Expense")

        if submit:

            st.success("Expense Added Successfully!")
