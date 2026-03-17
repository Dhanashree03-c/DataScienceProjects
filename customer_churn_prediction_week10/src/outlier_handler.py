"""
This module provides robust and reusable utilities for detecting and handling
outliers using statistical techniques such as:

1. Interquartile Range (IQR)
2. Z-score method

The implementation follows best practices:
- Input validation
- Edge case handling
- Reusability
- Clear documentation
"""

import pandas as pd
import numpy as np

def _validate_input(df: pd.DataFrame, column: str) -> None:
    """
    Internal helper function to validate input data.

    Raises:
        ValueError: If column does not exist or is non-numeric
    """

    # Check if column exists
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")

    # Check if column is numeric
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' must be numeric.")

def _compute_iqr_bounds(df: pd.DataFrame, column: str) -> tuple:
    """
    Compute IQR bounds for a given column.

    Returns:
        tuple: (lower_bound, upper_bound)
    """

    # Calculate quartiles
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    # Compute Interquartile Range
    IQR = Q3 - Q1

    # Define lower and upper bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    return lower_bound, upper_bound

def detect_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Detect outliers using the IQR method.

    Parameters:
        df (pd.DataFrame): Input dataset
        column (str): Column to analyze

    Returns:
        pd.DataFrame: Rows identified as outliers
    """

    # Validate input
    _validate_input(df, column)

    # Compute IQR bounds
    lower, upper = _compute_iqr_bounds(df, column)

    # Identify outliers
    outliers = df[(df[column] < lower) | (df[column] > upper)]

    return outliers


def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove outliers using IQR filtering.

    Parameters:
        df (pd.DataFrame): Input dataset
        column (str): Column to clean

    Returns:
        pd.DataFrame: Cleaned dataset with outliers removed
    """

    # Validate input
    _validate_input(df, column)

    # Compute bounds
    lower, upper = _compute_iqr_bounds(df, column)

    # Filter dataset to keep only valid values
    filtered_df = df[(df[column] >= lower) & (df[column] <= upper)].copy()

    return filtered_df


def cap_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Cap (clip) outliers instead of removing them.
    Useful when data loss is not acceptable.

    Parameters:
        df (pd.DataFrame): Input dataset
        column (str): Column to cap

    Returns:
        pd.DataFrame: Dataset with capped values
    """

    # Validate input
    _validate_input(df, column)

    # Compute bounds
    lower, upper = _compute_iqr_bounds(df, column)

    # Create a copy to avoid modifying original data
    df_copy = df.copy()

    # Clip values to the IQR range
    df_copy[column] = df_copy[column].clip(lower, upper)

    return df_copy


def detect_outliers_zscore(
    df: pd.DataFrame,
    column: str,
    threshold: float = 3.0
) -> pd.DataFrame:
    """
    Detect outliers using the Z-score method.

    Parameters:
        df (pd.DataFrame): Input dataset
        column (str): Column to analyze
        threshold (float): Z-score cutoff (default = 3.0)

    Returns:
        pd.DataFrame: Rows identified as outliers
    """

    # Validate input
    _validate_input(df, column)

    # Drop NaN values for safe computation
    series = df[column].dropna()

    # Compute mean and standard deviation
    mean = np.mean(series)
    std = np.std(series)

    # Handle edge case: zero standard deviation
    if std == 0:
        return pd.DataFrame()  # No variation → no outliers

    # Calculate Z-scores
    z_scores = np.abs((df[column] - mean) / std)

    # Return rows exceeding threshold
    return df[z_scores > threshold]


def remove_outliers_zscore(
    df: pd.DataFrame,
    column: str,
    threshold: float = 3.0
) -> pd.DataFrame:
    """
    Remove outliers using Z-score filtering.

    Parameters:
        df (pd.DataFrame): Input dataset
        column (str): Column to clean
        threshold (float): Z-score cutoff

    Returns:
        pd.DataFrame: Cleaned dataset
    """

    # Validate input
    _validate_input(df, column)

    # Compute mean and std
    mean = df[column].mean()
    std = df[column].std()

    # Handle zero std case
    if std == 0:
        return df.copy()

    # Compute Z-scores
    z_scores = np.abs((df[column] - mean) / std)

    # Filter valid rows
    filtered_df = df[z_scores <= threshold].copy()

    return filtered_df