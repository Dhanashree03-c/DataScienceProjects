"""
Handles categorical encoding and feature scaling.

This module provides reusable preprocessing utilities that
can be integrated into ML pipelines.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler


def apply_label_encoding(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply Label Encoding to specified categorical columns.

    Label Encoding converts categories into integer labels.
    """

    # Create a copy to avoid modifying original DataFrame
    df = df.copy()

    # Loop through each column separately
    for col in columns:
        encoder = LabelEncoder()  # Create a new encoder per column (IMPORTANT)
        
        # Convert column values into numeric labels
        df[col] = encoder.fit_transform(df[col].astype(str))

    return df


def apply_one_hot_encoding(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply One-Hot Encoding to categorical columns.

    Each category becomes a binary column.
    """

    # pd.get_dummies automatically handles encoding
    # drop_first=True avoids multicollinearity (dummy variable trap)
    df = pd.get_dummies(df, columns=columns, drop_first=True)

    return df


def apply_binary_encoding(df: pd.DataFrame, column: str, positive_value: str) -> pd.DataFrame:
    """
    Perform simple binary encoding.

    Converts a categorical column into 0/1 based on a condition.
    """

    # Copy to prevent modifying original dataset
    df = df.copy()

    # Create new binary column
    df[column + "_binary"] = df[column].apply(
        lambda x: 1 if x == positive_value else 0
    )

    # Drop original column after encoding
    df.drop(columns=[column], inplace=True)

    return df


def apply_standard_scaling(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply StandardScaler to numerical columns.

    Standardization:
    mean = 0, std = 1
    """

    # Copy dataset
    df = df.copy()

    # Initialize scaler
    scaler = StandardScaler()

    # Fit and transform selected columns
    df[columns] = scaler.fit_transform(df[columns])

    return df


def apply_minmax_scaling(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply MinMax scaling to numerical features.

    Scales values to range [0,1]
    """

    # Copy dataset
    df = df.copy()

    # Initialize scaler
    scaler = MinMaxScaler()

    # Apply transformation
    df[columns] = scaler.fit_transform(df[columns])

    return df