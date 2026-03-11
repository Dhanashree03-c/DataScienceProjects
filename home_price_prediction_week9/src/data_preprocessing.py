"""
Data Preprocessing Module
Responsible for loading data, feature selection,
encoding categorical variables and splitting dataset.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.
    """
    return pd.read_csv(path)


def prepare_features(data: pd.DataFrame):
    """
    Separate features and target variable.
    """
    X = data.drop(columns=["Property_ID", "Price"])
    y = data["Price"]
    return X, y


def create_preprocessor(categorical_features):
    """
    Create preprocessing pipeline for categorical variables.
    """
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ],
        remainder="passthrough"
    )
    return preprocessor


def split_dataset(X, y, test_size=0.2, random_state=42):
    """
    Split dataset into training and testing sets.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )