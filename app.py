import streamlit as st
from modules.auth import login_signup
from modules.dashboard import show_dashboard

# ---------------- SESSION STATE ---------------- #

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user_email" not in st.session_state:
    st.session_state["user_email"] = "Guest User"

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Finance Expense Tracker",
    layout="wide"
)

# ---------------- MAIN APP ---------------- #

if not st.session_state["logged_in"]:

    login_signup()

else:

    st.sidebar.success(
        f"Logged in as:\n{st.session_state['user_email']}"
    )

    if st.sidebar.button("Logout"):

        st.session_state["logged_in"] = False
        st.session_state["user_email"] = "Guest User"

        st.rerun()

    show_dashboard()
