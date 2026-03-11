"""
Data Preprocessing Module
Handles loading dataset, cleaning, encoding and train-test splitting
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.

    Args:
        file_path (str): Path to dataset.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    data = pd.read_csv(file_path)
    return data


def prepare_features(data: pd.DataFrame):
    """
    Separate features and target variable.

    Args:
        data (pd.DataFrame)

    Returns:
        X, y
    """

    X = data.drop(columns=["Property_ID", "Price"])
    y = data["Price"]

    return X, y


def create_preprocessor(categorical_features):
    """
    Create preprocessing pipeline for categorical variables.

    Args:
        categorical_features (list)

    Returns:
        ColumnTransformer
    """

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ],
        remainder="passthrough"
    )

    return preprocessor


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split dataset into training and testing sets.

    Returns:
        X_train, X_test, y_train, y_test
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )