import streamlit as st
import os

def show_prediction():

    st.title("🤖 Fraud Prediction")

    model_path = "models/expense_prediction_model.pkl"

    # CHECK MODEL EXISTS

    if not os.path.exists(model_path):

        st.warning(
            "Prediction model not found."
        )

        st.info(
            "Upload expense_prediction_model.pkl into models folder."
        )

        return

    import joblib
    import pandas as pd

    model = joblib.load(model_path)

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

            st.error("⚠ Fraudulent Transaction")

        else:

            st.success("✅ Legitimate Transaction")
