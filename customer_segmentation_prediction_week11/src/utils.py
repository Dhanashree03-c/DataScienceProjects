"""
Utility functions and project-wide constants.

This module centralizes reusable configuration such as
random seeds, project paths, and directory management.
"""

import os
import numpy as np

RANDOM_STATE = 42
OPTIMAL_CLUSTERS = 3

# PROJECT PATHS

DATA_RAW_PATH = "../data/raw/customer_churn.csv"
DATA_PROCESSED_PATH = "../data/processed/segmentation_data.csv"

RESULTS_DIR = "../results"
MODELS_DIR = "../results/models"

MODEL_RESULTS_PATH = "../results/model_evaluation_results.csv"

# DIRECTORY UTILITIES

# Ensure that the results and models directories exist
def ensure_directory(path: str) -> None:
    
    os.makedirs(path, exist_ok=True)

def set_random_seed(seed: int = RANDOM_STATE):
    """
    Set random seed for reproducibility.

    Parameters
    ----------
    seed : int
    """
    np.random.seed(seed)