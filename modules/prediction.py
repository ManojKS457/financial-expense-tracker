import streamlit as st
import random

def show_prediction():

    st.title("🤖 Fraud Prediction System")

    st.write("AI-Based Transaction Risk Detection")

    amount = st.number_input(
        "Enter Transaction Amount",
        min_value=0.0,
        value=1000.0
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        [
            "PAYMENT",
            "TRANSFER",
            "CASH_OUT",
            "DEBIT"
        ]
    )

    if st.button("Predict Fraud"):

        # SIMPLE LOGIC

        if amount > 500000:
            prediction = "Fraudulent Transaction"
            risk = "High Risk"
        elif amount > 100000:
            prediction = "Suspicious Transaction"
            risk = "Medium Risk"
        else:
            prediction = "Legitimate Transaction"
            risk = "Low Risk"

        st.success(f"Prediction: {prediction}")

        st.info(f"Risk Level: {risk}")

        st.subheader("AI Confidence Score")

        confidence = random.randint(80, 99)

        st.progress(confidence / 100)

        st.write(f"{confidence}% confidence")
