import streamlit as st

from modules.dashboard import show_dashboard
from modules.analytics import show_analytics
from modules.reports import show_reports
from modules.prediction import show_prediction
from modules.add_expense import show_add_expense
from modules.alerts import show_alerts

st.set_page_config(
    page_title="Finance Expense Tracker",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2830/2830284.png",
    width=80
)

st.sidebar.title("💰 Finance Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Add Expense",
        "Analytics",
        "Reports",
        "Predictions",
        "Alerts"
    ]
)

st.sidebar.success("Logged in as: admin@gmail.com")

if st.sidebar.button("Logout"):
    st.warning("Logged out successfully!")

# ---------------- PAGES ---------------- #

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

elif menu == "Alerts":
    show_alerts()
