import streamlit as st

from modules.dashboard import show_dashboard
from modules.analytics import show_analytics
from modules.reports import show_reports
from modules.prediction import show_prediction
from modules.add_expense import show_add_expense

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Finance Expense Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2489/2489756.png",
    width=100
)

st.sidebar.title("💰 Finance Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Expense",
        "Analytics",
        "Reports",
        "Predictions"
    ]
)

# ---------------- PAGE NAVIGATION ---------------- #

if menu == "Dashboard":

    show_dashboard()

elif menu == "Add Expense":

    show_add_expense()

elif menu == "Analytics":

    show_analytics()

elif menu == "Reports":

    show_reports()

elif menu == "Predictions":

    show_prediction()
