import streamlit as st
import sqlite3
import hashlib

# Database connection
conn = sqlite3.connect(
    "database/users.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()


# Password hashing
def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# Create user
def create_user(email, password):

    try:

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (
                email,
                hash_password(password)
            )
        )

        conn.commit()

        return True

    except:

        return False


# Login user
def login_user(email, password):

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (
            email,
            hash_password(password)
        )
    )

    data = cursor.fetchone()

    return data


# Authentication UI
def login_signup():

    st.title("🔐 Secure Authentication")

    option = st.selectbox(
        "Choose Option",
        [
            "Login",
            "Sign Up"
        ]
    )

    # LOGIN
    if option == "Login":

        st.subheader("Login")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            result = login_user(
                email,
                password
            )

            if result:

                st.session_state["logged_in"] = True
                st.session_state["user_email"] = email

                st.success(
                    "Login Successful!"
                )

            else:

                st.error(
                    "Invalid Email or Password"
                )

    # SIGNUP
    else:

        st.subheader("Create Account")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button("Create Account"):

            if password != confirm_password:

                st.error(
                    "Passwords do not match"
                )

            else:

                success = create_user(
                    email,
                    password
                )

                if success:

                    st.success(
                        "Account created successfully!"
                    )

                else:

                    st.error(
                        "Email already exists"
                    )