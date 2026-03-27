"""
Model evaluation utilities.
"""

import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

# Compute evaluation metrics
def calculate_metrics(y_true, preds, probs):

    return {

        "Accuracy": accuracy_score(y_true, preds),

        "Precision": precision_score(
            y_true,
            preds,
            zero_division=0
        ),

        "Recall": recall_score(
            y_true,
            preds,
            zero_division=0
        ),

        "F1": f1_score(
            y_true,
            preds,
            zero_division=0
        ),

        "ROC_AUC": roc_auc_score(y_true, probs)
    }


def save_evaluation_results(df: pd.DataFrame,
                            path: str):

    df.to_csv(path, index=False)

    print(f"Evaluation results saved to {path}")