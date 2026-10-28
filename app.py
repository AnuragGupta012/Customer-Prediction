import streamlit as st
from utils.style import load_css
from utils.sidebar import sidebar

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

load_css()
sidebar()

# -----------------------------
# Hero Section
# -----------------------------

st.title("📊 Customer Churn Prediction Dashboard")

st.markdown(
    "<h3 style='text-align:center;'>Predict • Analyze • Retain Customers</h3>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# KPI Cards
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("👥 Customers", "7043")

with col2:
    st.metric("🎯 Accuracy", "82%")

with col3:
    st.metric("🤖 Algorithm", "Random Forest")

st.markdown("---")

# -----------------------------
# Project Description
# -----------------------------

st.header("📌 Project Overview")

st.write("""
Customer Churn Prediction is a Machine Learning application that predicts
whether a telecom customer is likely to leave the company.

It helps businesses identify at-risk customers so they can improve customer
retention through proactive actions.
""")

st.markdown("---")

# -----------------------------
# Features
# -----------------------------

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.success("📊 Interactive Dashboard")

    st.success("🤖 Customer Churn Prediction")

    st.success("📈 Data Analytics")

with col2:

    st.success("🧠 Machine Learning")

    st.success("📄 Prediction Reports")

    st.success("📜 Prediction History")

st.markdown("---")

# -----------------------------
# Model Information
# -----------------------------

st.header("🧠 Machine Learning Model")

col1, col2 = st.columns(2)

with col1:

    st.info("Model : Random Forest Classifier")

    st.info("Dataset : IBM Telco Customer Churn")

with col2:

    st.info("Language : Python")

    st.info("Framework : Streamlit")

st.markdown("---")

# -----------------------------
# Developer
# -----------------------------

st.header("👨‍💻 Developer")

st.write("**Anurag Gupta**")

st.write("B.Tech Computer Science & Engineering")

st.write("Final Year")

st.markdown("---")

st.caption("© 2026 Customer Churn Prediction Dashboard")