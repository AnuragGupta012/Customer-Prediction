import streamlit as st


import streamlit as st
from utils.style import load_css

load_css()

from utils.sidebar import sidebar

load_css()
sidebar()

st.title("🤖 Customer Churn Prediction")

st.title("ℹ About Project")

st.markdown("""
# Customer Churn Prediction Dashboard

### Developed Using

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Plotly
- Matplotlib

---

### Machine Learning Model

Random Forest Classifier

---

### Dataset

IBM Telco Customer Churn Dataset

---

### Objective

Predict whether a telecom customer is likely to churn.

---

### Features

✔ Interactive Dashboard

✔ Customer Churn Prediction

✔ Analytics

✔ Machine Learning

✔ Business Recommendations
""")
