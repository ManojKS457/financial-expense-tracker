import streamlit as st

from modules.auth import login_signup
from modules.dashboard import show_dashboard
from modules.analytics import show_analytics
from modules.prediction import show_prediction
from modules.alerts import show_alerts
from modules.add_expense import show_add_expense
from modules.reports import show_reports

st.set_page_config(
    page_title="AI Financial Dashboard",
    page_icon="💰",
    layout="wide"
)

# Load CSS
def load_css():

    with open("assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# Authentication
if not st.session_state["logged_in"]:

    login_signup()

else:

    # Sidebar
    st.sidebar.image(
        "https://cdn-icons-png.flaticon.com/512/2489/2489756.png",
        width=80
    )

    st.sidebar.title("💰 Finance Dashboard")

    st.sidebar.success(
        f"Logged in as:\n{st.session_state['user_email']}"
    )

    st.sidebar.markdown("---")

    if st.sidebar.button("🔓 Logout"):

        st.session_state["logged_in"] = False

        st.rerun()

    page = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Analytics",
            "Prediction",
            "Alerts",
            "Add Transaction",
            "Reports"
        ]
    )

    if page == "Dashboard":
        show_dashboard()

    elif page == "Analytics":
        show_analytics()

    elif page == "Prediction":
        show_prediction()

    elif page == "Alerts":
        show_alerts()

    elif page == "Add Transaction":
        show_add_expense()

    elif page == "Reports":
        show_reports()