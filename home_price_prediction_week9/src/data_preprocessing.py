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
    Separate the dataset into input features (X) and target variable (y).

    Features include:
        Area, Bedrooms, Bathrooms, Age, Location, Property_Type

    Target variable:
        Price (house price)
    """
    #Remove non-predictive columns and the target column from feature set
    X = data.drop(columns=["Property_ID", "Price"])
    y = data["Price"]
    return X, y


def create_preprocessor(categorical_features):
    """
    Create a preprocessing pipeline for categorical features.

    Machine learning models cannot work directly with text categories
    like 'City Center' or 'Apartment'. Therefore we convert them into
    numerical format using One-Hot Encoding.
    """
    preprocessor = ColumnTransformer(
        transformers=[
            #Apply One-Hot Encoding to categorical columns
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ],
        #Keep remaining numerical columns unchanged
        remainder="passthrough"
    )
    return preprocessor


def split_dataset(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.

    Training data:
        Used to train the machine learning model.

    Testing data:
        Used to evaluate model performance on unseen data.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )