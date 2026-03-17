# Feature Engineering Module
# This module creates new informative features from existing dataset attributes.
import pandas as pd

def create_customer_lifetime_value(df: pd.DataFrame) -> pd.DataFrame:
    """
    Estimate customer lifetime value.

    Formula:
    CLV = Tenure * MonthlyCharges
    """

    # Create a copy to avoid modifying the original dataframe
    df = df.copy()

    # Compute lifetime value based on duration and spending
    df["CustomerLifetimeValue"] = df["Tenure"] * df["MonthlyCharges"]

    return df

# Calculate average monthly revenue per customer.
# Adds +1 to tenure to avoid division by zero for new customers.
def create_avg_revenue(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()  # Defensive copy to prevent side effects
    
    # Compute average revenue normalized by tenure
    df["AvgRevenuePerMonth"] = df["TotalCharges"] / (df["Tenure"] + 1)

    return df

def create_payment_efficiency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Measure payment efficiency.

    Ratio:
    TotalCharges / MonthlyCharges

    Indicates how consistently a customer pays over time.
    """

    df = df.copy()

    # Higher value may indicate long-term consistent payments
    df["PaymentEfficiency"] = df["TotalCharges"] / df["MonthlyCharges"]

    return df

def create_charge_difference(df: pd.DataFrame) -> pd.DataFrame:
    """
    Measure deviation between expected and actual charges.

    Expected Charges = MonthlyCharges * Tenure
    """

    df = df.copy()

    # Difference helps identify billing anomalies or irregular usage patterns
    df["ChargeDifference"] = df["TotalCharges"] - (
        df["MonthlyCharges"] * df["Tenure"]
    )

    return df

# Interaction feature combining customer age group and contract type.
def create_senior_contract_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create interaction feature between SeniorCitizen and contract type.

    Captures whether senior citizens prefer long-term contracts.
    """

    df = df.copy()

    # Ensure required encoded column exists before creating interaction
    if "Contract_Two year" in df.columns:
        df["SeniorCitizenContract"] = df["SeniorCitizen"] * df["Contract_Two year"]

    return df

def apply_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all feature engineering transformations sequentially.

    This wrapper improves:
    - Code readability
    - Reusability
    - Pipeline integration
    """

    # Apply each transformation step-by-step
    df = create_customer_lifetime_value(df)
    df = create_avg_revenue(df)
    df = create_payment_efficiency(df)
    df = create_charge_difference(df)
    df = create_senior_contract_feature(df)

    return df