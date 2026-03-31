"""
Model Evaluation Module
-----------------------

Provides utilities for evaluating ML models.

Responsibilities
----------------
- Compute evaluation metrics
- Generate confusion matrix
- Compute ROC-AUC score

Author: Dhanashree Tankar
"""

import logging

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

logger = logging.getLogger(__name__)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.

    Returns
    -------
    dict
        Dictionary of evaluation metrics
    """

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, predictions)

    auc = roc_auc_score(y_test, probabilities)

    report = classification_report(y_test, predictions)

    cm = confusion_matrix(y_test, predictions)

    logger.info("Model evaluation completed")

    return {
        "accuracy": accuracy,
        "roc_auc": auc,
        "classification_report": report,
        "confusion_matrix": cm
    }