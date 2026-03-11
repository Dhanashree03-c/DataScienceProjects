"""
Model Evaluation Module
Provides regression evaluation metrics.
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regression(y_true, y_pred):
    """
    Calculate evaluation metrics.
    """

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    }


def print_metrics(model_name, metrics):

    print(f"\nModel: {model_name}")
    print("-" * 30)

    for metric, value in metrics.items():
        print(f"{metric}: {value:,.2f}")