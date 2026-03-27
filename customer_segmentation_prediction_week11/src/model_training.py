"""
Model training module.

Trains Random Forest models for each customer segment.
Includes hyperparameter tuning and model persistence.
"""

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

from utils import RANDOM_STATE, MODELS_DIR, ensure_directory
from evaluation import calculate_metrics


def train_segment_models(df: pd.DataFrame):

    ensure_directory(MODELS_DIR)

    results = []
    trained_models = {}

    segments = df["Cluster_KMeans"].unique()

    for seg in segments:

        print(f"\nTraining model for Segment {seg}")

        segment_df = df[df["Cluster_KMeans"] == seg]

        X = segment_df.drop(
            ["Churn","Cluster_KMeans","Cluster_Hierarchical","Cluster_DBSCAN"],
            axis=1
        )

        y = segment_df["Churn"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=0.2,
            random_state=RANDOM_STATE
        )

        param_grid = {
            "n_estimators":[100,200],
            "max_depth":[5,10,None],
            "min_samples_split":[2,5]
        }

        grid = GridSearchCV(
            RandomForestClassifier(random_state=RANDOM_STATE),
            param_grid,
            cv=3,
            scoring="f1",
            n_jobs=-1
        )

        grid.fit(X_train, y_train)

        best_model = grid.best_estimator_

        model_path = f"{MODELS_DIR}/model_segment_{seg}.pkl"

        joblib.dump(best_model, model_path)

        print(f"Model saved to {model_path}")

        trained_models[seg] = best_model

        preds = best_model.predict(X_test)
        probs = best_model.predict_proba(X_test)[:,1]

        metrics = calculate_metrics(y_test, preds, probs)

        metrics["Segment"] = seg
        metrics["Best_Params"] = grid.best_params_

        results.append(metrics)

    return pd.DataFrame(results), trained_models