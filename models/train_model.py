import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv(
    "data/expense_data.csv",
    nrows=10000
)

df["Index"] = np.arange(len(df))

X = df[["Index"]]

y = df["amount"]

model = LinearRegression()

model.fit(X, y)

joblib.dump(
    model,
    "models/expense_prediction_model.pkl"
)

print("Model trained successfully!")