"""
Model Evaluation Module
Provides metrics for regression models
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_model(y_true, y_pred):
    """
    Calculate regression evaluation metrics.

    Returns:
        dict of metrics
    """

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    metrics = {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    }

    return metrics


def print_metrics(model_name, metrics):
    """
    Print evaluation metrics in readable format.
    """

    print(f"\nModel: {model_name}")
    print("-" * 30)
    print(f"MAE: {metrics['MAE']:,.2f}")
    print(f"MSE: {metrics['MSE']:,.2f}")
    print(f"RMSE: {metrics['RMSE']:,.2f}")
    print(f"R2 Score: {metrics['R2']:.3f}")