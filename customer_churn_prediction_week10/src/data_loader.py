"""
Responsible for loading datasets and performing initial validation.

This module isolates file I/O operations from the rest of the pipeline
to maintain separation of concerns and improve maintainability.
"""

import pandas as pd
from pathlib import Path

#Load dataset from CSV file.
def load_dataset(file_path: str) -> pd.DataFrame:
    # Convert string path to Path object for OS-independent handling
    path = Path(file_path)

    # Validate file existence before attempting to read
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {file_path}")

    # Read dataset into DataFrame
    df = pd.read_csv(path)

    return df

#Validate dataset structure and basic integrity.
#This helps catch dataset problems early in the pipeline.
def validate_dataset(df: pd.DataFrame) -> None:
    
    # Check if dataset is empty
    if df.empty:
        raise ValueError("Dataset is empty.")

    # Ensure target column exists (critical for supervised learning)
    if "Churn" not in df.columns:
        raise ValueError("Target column 'Churn' is missing.")

    # Check for missing values (non-blocking warning)
    # Missing data is allowed but should be handled downstream
    if df.isnull().sum().sum() > 0:
        print("Warning: Dataset contains missing values.")