import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import plotly.express as px

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

import streamlit as st
from utils.style import load_css

load_css()

from utils.sidebar import sidebar

load_css()
sidebar()

st.title("🤖 Customer Churn Prediction")

st.title("📈 Model Analytics")

df = pd.read_csv("data/encoded_telco_churn.csv")

model = joblib.load("models/churn_model.pkl")

X = df.drop("Churn", axis=1)
y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

y_pred = model.predict(X_test)

st.subheader("Confusion Matrix")

cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(6,5))

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm
)

disp.plot(ax=ax)

st.pyplot(fig)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

st.metric(
    "Model Accuracy",
    f"{accuracy*100:.2f}%"
)

from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    y_pred,
    output_dict=True
)

report_df = pd.DataFrame(report).transpose()

st.subheader("Classification Report")

st.dataframe(report_df)

importance = pd.DataFrame({

    "Feature":X.columns,

    "Importance":model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

st.subheader("Top 10 Important Features")

fig = px.bar(
    importance.head(10),
    x="Importance",
    y="Feature",
    orientation="h"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Encoded Dataset")

st.dataframe(df.head())

st.subheader("Dataset Statistics")

st.dataframe(df.describe())

