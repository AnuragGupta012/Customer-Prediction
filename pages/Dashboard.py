import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
from utils.style import load_css

load_css()

from utils.sidebar import sidebar

load_css()
sidebar()


st.title("📊 Customer Churn Dashboard")

# Load Data
df = pd.read_csv("data/cleaned_telco_churn.csv")

# ===========================
# Sidebar Filters
# ===========================

st.sidebar.header("📌 Dashboard Filters")

selected_gender = st.sidebar.multiselect(
    "Gender",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

selected_contract = st.sidebar.multiselect(
    "Contract",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

selected_internet = st.sidebar.multiselect(
    "Internet Service",
    options=df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

filtered_df = df[
    (df["gender"].isin(selected_gender)) &
    (df["Contract"].isin(selected_contract)) &
    (df["InternetService"].isin(selected_internet))
]

st.subheader("📊 Dashboard Summary")

total = len(filtered_df)
churn = len(filtered_df[filtered_df["Churn"] == "Yes"])
active = len(filtered_df[filtered_df["Churn"] == "No"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Customers", total)

with col2:
    st.metric("Churned", churn)

with col3:
    st.metric("Active", active)

# ==========================
# KPI Cards
# ==========================
st.subheader("Customer Churn Distribution")

fig = px.pie(
    filtered_df,
    names="Churn",
    title="Customer Churn Distribution",
    color="Churn",
    hole=0.4
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Gender-wise Churn")

fig = px.histogram(
    filtered_df,
    x="gender",
    color="Churn",
    barmode="group"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Contract Type vs Churn")

fig = px.histogram(
    filtered_df,
    x="Contract",
    color="Churn"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Internet Service")

fig = px.histogram(
    filtered_df,
    x="InternetService",
    color="Churn"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Charges")

fig = px.box(
    filtered_df,
    x="Churn",
    y="MonthlyCharges",
    color="Churn"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Customer Tenure")

fig = px.histogram(
    filtered_df,
    x="tenure",
    color="Churn",
    nbins=30
)

st.plotly_chart(fig, use_container_width=True)

total_customers = len(df)
churned = len(df[df["Churn"] == "Yes"])
active = len(df[df["Churn"] == "No"])
churn_rate = (churned / total_customers) * 100

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Customers", total_customers)

with col2:
    st.metric("✅ Active Customers", active)

with col3:
    st.metric("❌ Churned Customers", churned)

with col4:
    st.metric("📈 Churn Rate", f"{churn_rate:.2f}%")

st.markdown("---")