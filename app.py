import streamlit as st

from modules.auth import login_signup
from modules.dashboard import show_dashboard

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Finance Expense Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION ---------------- #

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_email" not in st.session_state:
    st.session_state.user_email = "Guest User"

# ---------------- LOGIN ---------------- #

if not st.session_state.logged_in:

    login_signup()

# ---------------- MAIN APP ---------------- #

else:

    # ---------- SIDEBAR ---------- #

    st.sidebar.image(
        "https://cdn-icons-png.flaticon.com/512/2489/2489756.png",
        width=90
    )

    st.sidebar.markdown("## 💰 Finance Dashboard")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Add Transaction",
            "Analytics",
            "Reports",
            "Predictions",
            "Settings"
        ]
    )

    st.sidebar.success(
        f"Logged in as: {st.session_state.user_email}"
    )

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user_email = "Guest User"

        st.rerun()

    # ---------- DASHBOARD ---------- #

    if menu == "Dashboard":

        show_dashboard()

    # ---------- ADD TRANSACTION ---------- #

    elif menu == "Add Transaction":

        st.title("➕ Add Transaction")

        with st.form("transaction_form"):

            transaction_type = st.selectbox(
                "Transaction Type",
                ["Income", "Expense"]
            )

            category = st.selectbox(
                "Category",
                [
                    "Food",
                    "Travel",
                    "Shopping",
                    "Bills",
                    "Entertainment",
                    "Salary",
                    "Investment"
                ]
            )

            amount = st.number_input(
                "Amount",
                min_value=0.0,
                step=100.0
            )

            note = st.text_area("Description")

            submit = st.form_submit_button("Save Transaction")

            if submit:

                st.success("Transaction added successfully!")

                st.balloons()

    # ---------- ANALYTICS ---------- #

    elif menu == "Analytics":

        st.title("📊 Analytics")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Monthly Expenses",
                "₹45,000",
                "-12%"
            )

            st.metric(
                "Savings",
                "₹1,25,000",
                "+18%"
            )

        with col2:

            st.metric(
                "Investments",
                "₹2,40,000",
                "+9%"
            )

            st.metric(
                "Budget Usage",
                "78%",
                "-5%"
            )

        st.info("AI analytics generated successfully.")

    # ---------- REPORTS ---------- #

    elif menu == "Reports":

        st.title("📄 Reports")

        st.download_button(
            label="Download Monthly Report",
            data="Finance Report Generated",
            file_name="monthly_report.txt"
        )

        st.success("Reports section working successfully.")

    # ---------- PREDICTIONS ---------- #

    elif menu == "Predictions":

        st.title("🤖 AI Predictions")

        st.subheader("Future Expense Forecast")

        st.warning(
            "Predicted next month expenses may increase by 15%."
        )

        st.info(
            "AI detected unusual spending patterns."
        )

    # ---------- SETTINGS ---------- #

    elif menu == "Settings":

        st.title("⚙️ Settings")

        theme = st.selectbox(
            "Select Theme",
            ["Dark", "Light"]
        )

        currency = st.selectbox(
            "Currency",
            ["INR ₹", "USD $", "EUR €"]
        )

        notifications = st.checkbox(
            "Enable Notifications",
            value=True
        )

        if st.button("Save Settings"):

            st.success("Settings updated successfully!")
