import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

def show_prediction():

    st.header("🤖 Future Expense Prediction")

    df = pd.read_csv(
        "data/sample_expense_data.csv"
    )

    df["Index"] = np.arange(len(df))

    X = df[["Index"]]

    y = df["amount"]

    model = LinearRegression()

    model.fit(X, y)

    future_index = np.array([[len(df) + 1]])

    prediction = model.predict(future_index)

    st.success(
        f"Predicted Future Transaction Amount: ₹{prediction[0]:,.2f}"
    )

    df["Predicted"] = model.predict(X)

    fig = px.line(
        df.head(200),
        x="Index",
        y=["amount", "Predicted"],
        title="Actual vs Predicted Transactions"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )