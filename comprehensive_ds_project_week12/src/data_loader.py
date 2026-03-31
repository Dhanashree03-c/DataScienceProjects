"""
Data Loading Module
-------------------

Handles loading and saving datasets for the ML pipeline.

Responsibilities
----------------
- Load CSV datasets
- Save processed datasets
- Validate file paths

Author: Dhanashree Tankar
"""

import os
import logging
import pandas as pd

logger = logging.getLogger(__name__)


def load_csv(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file.

    Parameters
    ----------
    path : str
        File path to CSV dataset

    Returns
    -------
    pd.DataFrame
        Loaded dataset
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}")

    df = pd.read_csv(path)

    logger.info("Dataset loaded successfully")
    logger.info("Dataset shape: %s", df.shape)

    return df


def save_csv(df: pd.DataFrame, path: str) -> None:
    """
    Save dataframe to CSV file.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset to save

    path : str
        Output path
    """

    os.makedirs(os.path.dirname(path), exist_ok=True)

    df.to_csv(path, index=False)

    logger.info("Dataset saved to %s", path)