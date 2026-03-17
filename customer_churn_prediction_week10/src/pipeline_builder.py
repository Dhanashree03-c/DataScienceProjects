"""
Builds the end-to-end preprocessing and machine learning pipeline.

Encapsulating pipeline logic improves reproducibility, maintainability,
and ensures consistent transformations during both training and inference.
"""

# Core sklearn utilities for building pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Preprocessing tools
from sklearn.preprocessing import StandardScaler

# Machine learning model
from sklearn.ensemble import RandomForestClassifier


def build_preprocessing_pipeline(numeric_features: list):
    """
    Construct a preprocessing pipeline specifically for numerical features.

    This function standardizes numerical inputs using StandardScaler,
    which transforms features to have mean=0 and variance=1.
    This is important for improving model convergence and stability.

    Parameters
    ----------
    numeric_features : list
        List of column names representing numerical features.

    Returns
    -------
    ColumnTransformer
        A transformer that applies scaling to numerical columns.
    """

    # Define transformation pipeline for numerical features
    numeric_transformer = Pipeline(
        steps=[
            # Standardize numerical features (Z-score normalization)
            ("scaler", StandardScaler())
        ]
    )

    # ColumnTransformer applies transformations selectively to columns
    preprocessor = ColumnTransformer(
        transformers=[
            # Apply numeric_transformer to numeric_features only
            ("num", numeric_transformer, numeric_features)
        ]
    )

    return preprocessor


def build_model_pipeline(preprocessor):
    """
    Combine preprocessing and model into a single unified pipeline.

    This ensures:
    - Same preprocessing is applied during training and inference
    - Prevents data leakage
    - Simplifies deployment and reproducibility

    Parameters
    ----------
    preprocessor : ColumnTransformer
        Preprocessing pipeline created using build_preprocessing_pipeline()

    Returns
    -------
    Pipeline
        Complete machine learning pipeline including preprocessing and model
    """

    # Define full pipeline: preprocessing + model
    pipeline = Pipeline(
        steps=[
            # Step 1: Apply preprocessing transformations
            ("preprocessing", preprocessor),

            # Step 2: Train Random Forest classifier
            ("model", RandomForestClassifier(
                n_estimators=100,   # Number of trees in the forest
                random_state=42     # Ensures reproducibility of results
            ))
        ]
    )

    return pipeline