import streamlit as st
from utils.email_sender import send_email


def show_alerts():

    st.title("📧 Email Alerts")

    receiver_email = st.text_input("Enter Email Address")

    if st.button("Send Budget Alert"):

        subject = "Budget Alert - Finance Tracker"

        body = """
Hello User,

Your monthly budget limit has been exceeded.

Please review your expenses immediately.

- Finance Expense Tracker
"""

        success = send_email(subject, body, receiver_email)

        if success:
            st.success("Email Sent Successfully!")
        else:
            st.error("Failed to Send Email")
