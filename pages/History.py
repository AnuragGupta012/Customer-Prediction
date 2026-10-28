import streamlit as st
import pandas as pd
import os

from utils.style import load_css
from utils.sidebar import sidebar

load_css()
sidebar()

st.title("📜 Prediction History")

file_path = "history/prediction_history.csv"

if not os.path.exists(file_path):
    st.info("No prediction history found.")
    st.stop()

history = pd.read_csv(file_path)

# ============================
# Summary Cards
# ============================

total = len(history)
churn = len(history[history["Prediction"] == "Churn"])
stay = len(history[history["Prediction"] == "No Churn"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Predictions", total)

with col2:
    st.metric("Churn", churn)

with col3:
    st.metric("No Churn", stay)

st.markdown("---")

# ============================
# Filters
# ============================

st.subheader("🔍 Filter Predictions")

prediction_filter = st.selectbox(
    "Prediction",
    ["All", "Churn", "No Churn"]
)

if prediction_filter != "All":
    history = history[
        history["Prediction"] == prediction_filter
    ]

st.dataframe(history, use_container_width=True)

st.markdown("---")

# ============================
# Download CSV
# ============================

csv = history.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download History",
    csv,
    "prediction_history.csv",
    "text/csv"
)

# ============================
# Clear History
# ============================

if st.button("🗑 Clear History"):

    history.iloc[0:0].to_csv(file_path, index=False)

    st.success("History Cleared Successfully!")

    st.rerun()