import joblib
import numpy as np

model = joblib.load(
    "models/expense_prediction_model.pkl"
)

def predict_transaction(index):

    prediction = model.predict(
        np.array([[index]])
    )

    return prediction[0]