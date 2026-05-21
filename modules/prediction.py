import streamlit as st
import pandas as pd
import joblib

def show_prediction():

    st.title("🤖 Fraud Prediction")

    model = joblib.load(
        "models/expense_prediction_model.pkl"
    )

    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0
    )

    oldbalanceOrg = st.number_input(
        "Old Balance Sender",
        min_value=0.0
    )

    newbalanceOrig = st.number_input(
        "New Balance Sender",
        min_value=0.0
    )

    oldbalanceDest = st.number_input(
        "Old Balance Receiver",
        min_value=0.0
    )

    newbalanceDest = st.number_input(
        "New Balance Receiver",
        min_value=0.0
    )

    if st.button("Predict Fraud"):

        input_data = pd.DataFrame([[
            amount,
            oldbalanceOrg,
            newbalanceOrig,
            oldbalanceDest,
            newbalanceDest
        ]])

        prediction = model.predict(input_data)

        if prediction[0] == 1:

            st.error("⚠ Fraudulent Transaction Detected")

        else:

            st.success("✅ Legitimate Transaction")
