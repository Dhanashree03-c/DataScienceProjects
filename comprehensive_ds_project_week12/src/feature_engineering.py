"""
Feature Engineering Module

Responsible for constructing the feature matrix (X)
and target vector (y) used for machine learning models.
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


def create_features(df: pd.DataFrame):
    """
    Generate feature matrix and target variable.

    Parameters
    ----------
    df : pd.DataFrame
        Preprocessed dataset

    Returns
    -------
    X : pd.DataFrame
        Feature matrix

    y : pd.Series
        Target variable
    """

    if "Churn" not in df.columns:
        raise ValueError("Target column 'Churn' not found in dataset")

    # Target variable
    y = df["Churn"]

    # Feature matrix (remove target)
    X = df.drop(columns=["Churn"], errors="ignore")

    # Remove identifier columns if still present
    if "CustomerID" in X.columns:
        X = X.drop(columns=["CustomerID"])

    logger.info("Feature engineering completed")
    logger.info(f"Feature matrix shape: {X.shape}")

    return X, y