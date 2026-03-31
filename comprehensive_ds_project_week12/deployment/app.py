"""
Customer Churn Prediction App
--------------------------------
Streamlit web application for predicting telecom customer churn.

Author: Dhanashree Tankar
"""

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📉",
    layout="wide"
)

# -------------------------------------------------------
# LOAD MODEL
# -------------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("deployment/model.pkl")
    return model

model = load_model()

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("📉 Customer Churn Prediction System")

st.markdown("""
Predict whether a telecom customer is likely to **churn** based on subscription
details and behavioral attributes.

This tool can help companies identify **high-risk customers** and implement
retention strategies.
""")

st.divider()

# -------------------------------------------------------
# SIDEBAR INPUT
# -------------------------------------------------------

st.sidebar.header("Customer Information")

tenure = st.sidebar.slider(
    "Tenure (months)",
    0,
    72,
    12
)

monthly_charges = st.sidebar.slider(
    "Monthly Charges",
    10,
    150,
    70
)

total_charges = st.sidebar.slider(
    "Total Charges",
    0,
    10000,
    2000
)

senior_citizen = st.sidebar.selectbox(
    "Senior Citizen",
    [0,1]
)

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    [0,1]
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month","One year","Two year"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic Check","Credit Card","Bank Transfer"]
)

# -------------------------------------------------------
# FEATURE ENGINEERING
# -------------------------------------------------------

def create_input_dataframe():

    data = {
        "Tenure":[tenure],
        "MonthlyCharges":[monthly_charges],
        "TotalCharges":[total_charges],
        "PaperlessBilling":[paperless],
        "SeniorCitizen":[senior_citizen],
        "Contract_One year":[0],
        "Contract_Two year":[0],
        "PaymentMethod_Credit Card":[0],
        "PaymentMethod_Electronic Check":[0]
    }

    if contract == "One year":
        data["Contract_One year"] = [1]

    if contract == "Two year":
        data["Contract_Two year"] = [1]

    if payment == "Credit Card":
        data["PaymentMethod_Credit Card"] = [1]

    if payment == "Electronic Check":
        data["PaymentMethod_Electronic Check"] = [1]

    return pd.DataFrame(data)

# -------------------------------------------------------
# PREDICTION BUTTON
# -------------------------------------------------------

if st.button("Predict Churn"):

    input_df = create_input_dataframe()

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == 1:
            st.error("⚠️ Customer Likely To Churn")
        else:
            st.success("✅ Customer Likely To Stay")

    with col2:

        st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

    st.divider()

    # -------------------------------------------------------
    # RISK SEGMENTATION
    # -------------------------------------------------------

    if probability < 0.30:
        risk = "Low Risk"
        color = "green"

    elif probability < 0.70:
        risk = "Medium Risk"
        color = "orange"

    else:
        risk = "High Risk"
        color = "red"

    st.subheader("Risk Segment")

    st.markdown(f"### {risk}")

    # -------------------------------------------------------
    # SHOW INPUT DATA
    # -------------------------------------------------------

    st.subheader("Customer Profile")

    st.dataframe(input_df)

# -------------------------------------------------------
# PROJECT INFO
# -------------------------------------------------------

st.divider()

st.markdown("""
### About This Project

This machine learning model predicts telecom customer churn using:

- Logistic Regression
- Random Forest Classifier
- Feature engineering and preprocessing
- Hyperparameter tuning

**Goal:** Identify customers at risk of leaving and enable proactive retention strategies.

---

Author: **Dhanashree Tankar**

Data Science Capstone Project
""")