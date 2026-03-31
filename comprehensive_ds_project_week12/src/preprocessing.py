"""
Data Preprocessing Module

Responsible for cleaning and preparing the dataset before modeling.

Responsibilities

- Validate dataset schema
- Handle missing values
- Encode categorical variables
- Convert binary features
- Remove identifier columns
"""

import logging
from typing import List

import pandas as pd


logger = logging.getLogger(__name__)

# Validation
def validate_dataset(df: pd.DataFrame, required_columns: List[str]) -> None:
    """
    Validate that the dataset contains required columns.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataset

    required_columns : List[str]
        Columns that must exist in dataset
    """

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError(f"Dataset missing required columns: {missing}")

    logger.info("Dataset validation passed")

# Binary Feature Encoding
def encode_binary_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert binary categorical features into numeric format.

    Example:
        Yes/No -> 1/0
    """

    df = df.copy()

    binary_mappings = {
        "PaperlessBilling": {"Yes": 1, "No": 0}
    }

    for column, mapping in binary_mappings.items():
        if column in df.columns:
            df[column] = df[column].map(mapping)

    return df

# Categorical Encoding
def encode_categorical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform one-hot encoding for categorical variables.
    """

    df = df.copy()

    categorical_columns = [
        "Contract",
        "PaymentMethod"
    ]

    existing_columns = [c for c in categorical_columns if c in df.columns]

    df = pd.get_dummies(
        df,
        columns=existing_columns,
        drop_first=True,
        dtype = int
    )

    return df

# Missing Value Handling
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values in dataset.
    """

    df = df.copy()

    # Simple strategy for small datasets
    df = df.dropna()

    logger.info("Missing values removed")

    return df

# Remove Identifier Columns
def drop_identifier_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove columns that should not be used for modeling.
    """

    df = df.copy()

    id_columns = ["CustomerID"]

    existing_cols = [c for c in id_columns if c in df.columns]

    if existing_cols:
        df = df.drop(columns=existing_cols)

    return df

# Main Preprocessing Pipeline
def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Execute full preprocessing pipeline.

    Steps
    -----
    1. Validate dataset
    2. Encode binary features
    3. Encode categorical variables
    4. Handle missing values
    5. Drop identifier columns

    Returns
    -------
    pd.DataFrame
        Cleaned dataset ready for feature engineering
    """

    logger.info("Starting preprocessing pipeline")

    required_columns = [
        "CustomerID",
        "Contract",
        "PaymentMethod",
        "PaperlessBilling",
        "Churn"
    ]

    df = df.copy()
    
    validate_dataset(df, required_columns)

    df = encode_binary_features(df)

    df = encode_categorical_features(df)

    df = handle_missing_values(df)

    df = drop_identifier_columns(df)

    logger.info("Preprocessing completed")

    return df