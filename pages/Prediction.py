from utils.predictor import predict_churn
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import os

from utils.style import load_css
from utils.sidebar import sidebar

load_css()
sidebar()

st.title("🤖 Customer Churn Prediction")

st.write("Fill the customer details below.")

# ===========================
# Basic Information
# ===========================

gender = st.selectbox("Gender", ["Male", "Female"])

SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])

Partner = st.selectbox("Partner", ["Yes", "No"])

Dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider("Tenure (Months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["Yes", "No"])

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

MonthlyCharges = st.number_input(
    "Monthly Charges",
    0.0,
    200.0,
    70.0
)

TotalCharges = st.number_input(
    "Total Charges",
    0.0,
    10000.0,
    1000.0
)

MultipleLines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Bank transfer (automatic)",
        "Credit card (automatic)",
        "Electronic check",
        "Mailed check"
    ]
)

# ===========================
# Prediction Button
# ===========================

if st.button("Predict Churn"):

    input_data = {

        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": SeniorCitizen,
        "Partner": 1 if Partner == "Yes" else 0,
        "Dependents": 1 if Dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if PhoneService == "Yes" else 0,
        "PaperlessBilling": 1 if PaperlessBilling == "Yes" else 0,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,

        # Multiple Lines
        "MultipleLines_No phone service": 1 if MultipleLines == "No phone service" else 0,
        "MultipleLines_Yes": 1 if MultipleLines == "Yes" else 0,

        # Internet Service
        "InternetService_Fiber optic": 1 if InternetService == "Fiber optic" else 0,
        "InternetService_No": 1 if InternetService == "No" else 0,

        # Online Security
        "OnlineSecurity_No internet service": 1 if OnlineSecurity == "No internet service" else 0,
        "OnlineSecurity_Yes": 1 if OnlineSecurity == "Yes" else 0,

        # Online Backup
        "OnlineBackup_No internet service": 1 if OnlineBackup == "No internet service" else 0,
        "OnlineBackup_Yes": 1 if OnlineBackup == "Yes" else 0,

        # Device Protection
        "DeviceProtection_No internet service": 1 if DeviceProtection == "No internet service" else 0,
        "DeviceProtection_Yes": 1 if DeviceProtection == "Yes" else 0,

        # Tech Support
        "TechSupport_No internet service": 1 if TechSupport == "No internet service" else 0,
        "TechSupport_Yes": 1 if TechSupport == "Yes" else 0,

        # Streaming TV
        "StreamingTV_No internet service": 1 if StreamingTV == "No internet service" else 0,
        "StreamingTV_Yes": 1 if StreamingTV == "Yes" else 0,

        # Streaming Movies
        "StreamingMovies_No internet service": 1 if StreamingMovies == "No internet service" else 0,
        "StreamingMovies_Yes": 1 if StreamingMovies == "Yes" else 0,

        # Contract
        "Contract_One year": 1 if Contract == "One year" else 0,
        "Contract_Two year": 1 if Contract == "Two year" else 0,

        # Payment Method
        "PaymentMethod_Credit card (automatic)": 1 if PaymentMethod == "Credit card (automatic)" else 0,
        "PaymentMethod_Electronic check": 1 if PaymentMethod == "Electronic check" else 0,
        "PaymentMethod_Mailed check": 1 if PaymentMethod == "Mailed check" else 0
    }

    # ===========================
    # Prediction
    # ===========================

    prediction, probability = predict_churn(input_data)

    churn_probability = probability[1] * 100
    stay_probability = probability[0] * 100

    # ===========================
    # Save Prediction History
    # ===========================

    os.makedirs("history", exist_ok=True)

    history = pd.DataFrame([{
        "Gender": gender,
        "Senior Citizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "Tenure": tenure,
        "Monthly Charges": MonthlyCharges,
        "Prediction": "Churn" if prediction == 1 else "No Churn",
        "Probability (%)": round(churn_probability, 2)
    }])

    file_path = "history/prediction_history.csv"

    if os.path.exists(file_path):
        history.to_csv(
            file_path,
            mode="a",
            header=False,
            index=False
        )
    else:
        history.to_csv(
            file_path,
            index=False
        )

    # ===========================
    # Show Result
    # ===========================

    st.markdown("---")

    if prediction == 1:
        st.error("⚠️ Customer is likely to Churn")
    else:
        st.success("✅ Customer is likely to Stay")

    st.subheader("Prediction Probability")

    st.progress(int(churn_probability))

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=churn_probability,
            title={"text": "Churn Risk (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
                "steps": [
                    {"range": [0, 40], "color": "lightgreen"},
                    {"range": [40, 70], "color": "yellow"},
                    {"range": [70, 100], "color": "salmon"}
                ]
            }
        )
    )

    st.plotly_chart(fig, use_container_width=True)

    if churn_probability < 40:
        st.success("🟢 Low Risk Customer")
    elif churn_probability < 70:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.error("🔴 High Risk Customer")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Stay Probability",
            f"{stay_probability:.2f}%"
        )

    with col2:
        st.metric(
            "Churn Probability",
            f"{churn_probability:.2f}%"
        )

    st.markdown("---")

    st.subheader("📋 Customer Summary")

    summary = pd.DataFrame({
        "Field": [
            "Gender",
            "Tenure",
            "Contract",
            "Monthly Charges"
        ],
        "Value": [
            gender,
            tenure,
            Contract,
            MonthlyCharges
        ]
    })

    st.table(summary)

    st.subheader("Business Recommendation")

    if prediction == 1:
        st.warning("""
### Suggested Actions

- Offer a loyalty discount
- Contact the customer personally
- Provide a better service plan
- Offer a long-term contract
""")
    else:
        st.success("""
### Customer Status

✅ Customer appears satisfied.

Continue providing quality service and maintain engagement.
""")