"""
Data preprocessing module.

Handles:
- loading raw data
- encoding categorical variables
- cleaning dataset
- saving processed dataset
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from utils import DATA_RAW_PATH, DATA_PROCESSED_PATH, ensure_directory

# Load raw dataset
def load_raw_data(path: str = DATA_RAW_PATH) -> pd.DataFrame:

    df = pd.read_csv(path)
    print(f"Dataset loaded: {df.shape}")
    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform dataset.

    Steps
    -----
    - Drop identifier columns
    - Encode categorical features

    """

    df = df.copy()

    if "CustomerID" in df.columns:
        df.drop(columns=["CustomerID"], inplace=True)

    categorical_cols = df.select_dtypes(include="object").columns

    label_encoders = {}

    for col in categorical_cols:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])
        label_encoders[col] = encoder

    return df

# Save processed dataset
def save_processed_data(df: pd.DataFrame,
                        path: str = DATA_PROCESSED_PATH) -> None:

    ensure_directory("../data/processed")

    df.to_csv(path, index=False)

    print(f"Processed dataset saved to {path}")