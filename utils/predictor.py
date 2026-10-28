import joblib
import pandas as pd


# Load trained model
model = joblib.load("models/churn_model.pkl")


def predict_churn(input_data):
    """
    input_data -> dictionary containing all encoded features
    """

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    return prediction, probability