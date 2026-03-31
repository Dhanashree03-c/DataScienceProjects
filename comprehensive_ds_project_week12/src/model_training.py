"""
Model Training Module
---------------------

Handles model training and saving trained models.

Responsibilities
----------------
- Train ML models
- Perform hyperparameter tuning
- Save trained models

Author: Dhanashree Tankar
"""

import os
import logging
import joblib

from sklearn.model_selection import GridSearchCV

logger = logging.getLogger(__name__)


def tune_model(model, param_grid, X_train, y_train, cv=5):
    """
    Perform hyperparameter tuning using GridSearchCV.
    """

    logger.info("Starting hyperparameter tuning")

    grid_search = GridSearchCV(
        model,
        param_grid,
        cv=cv,
        scoring="roc_auc",
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)

    logger.info("Best parameters: %s", grid_search.best_params_)

    return grid_search.best_estimator_


def train_model(model, X_train, y_train):
    """
    Train model without hyperparameter tuning.
    """

    logger.info("Training model")

    model.fit(X_train, y_train)

    logger.info("Model training completed")

    return model


def save_model(model, path: str):
    """
    Save trained model to disk.
    """

    os.makedirs(os.path.dirname(path), exist_ok=True)

    joblib.dump(model, path)

    logger.info("Model saved to %s", path)