import streamlit as st
import sqlite3
import hashlib
import os

from streamlit_oauth import OAuth2Component

# CREATE DATABASE FOLDER
os.makedirs("database", exist_ok=True)

# DATABASE CONNECTION
conn = sqlite3.connect(
    "database/users.db",
    check_same_thread=False
)

cursor = conn.cursor()

# CREATE USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    name TEXT
)
""")

conn.commit()

# GOOGLE OAUTH ENV VARIABLES
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

# OAUTH COMPONENT
oauth2 = OAuth2Component(
    CLIENT_ID,
    CLIENT_SECRET,
    AUTHORIZE_URL,
    TOKEN_URL
)

def login_signup():

    st.markdown(
        """
        <h1 style='text-align:center;'>
        💰 Finance Expense Tracker
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h3 style='text-align:center;color:gray;'>
        Secure Login with Google OAuth
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    result = oauth2.authorize_button(
        name="🔵 Continue with Google",

        redirect_uri=REDIRECT_URI,

        scope="openid email profile",

        key="google",

        extras_params={
            "prompt": "consent",
            "access_type": "offline"
        },

        use_container_width=True
    )

    if result:

        token = result.get("token")

        if token:

            st.session_state["logged_in"] = True

            st.success(
                "Google Login Successful!"
            )

            st.rerun()
