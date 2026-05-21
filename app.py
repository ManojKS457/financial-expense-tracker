import streamlit as st

from modules.auth import login_signup
from modules.dashboard import show_dashboard

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Finance Expense Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE ---------------- #

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user_email" not in st.session_state:
    st.session_state["user_email"] = "Guest User"

# ---------------- LOGIN PAGE ---------------- #

if not st.session_state["logged_in"]:

    login_signup()

# ---------------- DASHBOARD ---------------- #

else:

    # ---------- SIDEBAR ---------- #

    st.sidebar.image(
        "https://cdn-icons-png.flaticon.com/512/2489/2489756.png",
        width=80
    )

    st.sidebar.markdown("## 💰 Finance Dashboard")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Analytics",
            "Reports",
            "Predictions",
            "Settings"
        ]
    )

    st.sidebar.success(
        f"Logged in as:\n{st.session_state['user_email']}"
    )

    if st.sidebar.button("Logout"):

        st.session_state["logged_in"] = False
        st.session_state["user_email"] = "Guest User"

        st.rerun()

    # ---------- MAIN CONTENT ---------- #

    if menu == "Dashboard":

        show_dashboard()

    elif menu == "Analytics":

        st.title("📊 Analytics")
        st.write("Analytics section coming soon.")

    elif menu == "Reports":

        st.title("📄 Reports")
        st.write("Reports section coming soon.")

    elif menu == "Predictions":

        st.title("🤖 Predictions")
        st.write("Prediction section coming soon.")

    elif menu == "Settings":

        st.title("⚙️ Settings")
        st.write("Settings section coming soon.")
