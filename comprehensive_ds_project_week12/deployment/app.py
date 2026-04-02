"""
Customer Churn Prediction Web App
Author: Dhanashree Tankar

Streamlit application for predicting customer churn
using a trained Random Forest model.
"""

# 1. IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import joblib
import logging

# 2. PAGE CONFIGURATION (MUST BE FIRST STREAMLIT COMMAND)
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📉",
    layout="centered"
)

# 3. CONFIGURATION
MODEL_PATH = "model.pkl"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 4. LOAD MODEL
@st.cache_resource
def load_model():
    """Load trained ML model"""
    try:
        model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully")
        return model
    except Exception as e:
        logger.error(f"Model loading failed: {e}")
        return None


model = load_model()

if model is None:
    st.error("❌ Error loading model. Please check model.pkl file.")

# 5. APP TITLE
st.title("📉 Customer Churn Prediction System")

st.write(
"""
This application predicts whether a telecom customer is likely to **churn**
based on subscription and behavioral information.

Provide the customer details in the sidebar and click **Predict Churn**.
"""
)

# 6. SIDEBAR INPUTS
st.sidebar.header("Customer Information")

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0, 72, 12
)

monthly_charges = st.sidebar.slider(
    "Monthly Charges ($)",
    10.0, 150.0, 70.0
)

total_charges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

paperless_billing = st.sidebar.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

senior_citizen = st.sidebar.selectbox(
    "Senior Citizen",
    ["Yes", "No"]
)

# 7. PREPROCESS USER INPUT
def preprocess_input():
    """Convert user input into model-ready dataframe"""

    data = {
        "Tenure": tenure,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "PaperlessBilling": 1 if paperless_billing == "Yes" else 0,
        "Contract": contract,
        "PaymentMethod": payment_method
    }

    df = pd.DataFrame([data])

    # Apply one-hot encoding
    df = pd.get_dummies(df)

    # Get feature names expected by model
    model_features = model.feature_names_in_

    # Add missing columns
    for col in model_features:
        if col not in df.columns:
            df[col] = 0

    # Keep only model features in correct order
    df = df[model_features]

    return df

# 8. PREDICTION
if st.button("Predict Churn"):

    if model is None:
        st.error("Model not available.")
    else:

        input_df = preprocess_input()

        try:

            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]

            st.subheader("Prediction Result")

            if prediction == 1:
                st.error("⚠️ Customer is likely to churn")
            else:
                st.success("✅ Customer likely to stay")

            st.metric(
                label="Churn Probability",
                value=f"{probability*100:.2f}%"
            )

        except Exception as e:
            st.error("Prediction failed")
            logger.error(e)

# 9. FOOTER
st.markdown("---")

st.caption(
"Machine Learning Capstone Project — Customer Churn Prediction"
)