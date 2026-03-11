"""
Model Training Module
Contains functions to train different machine learning models.
"""

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_linear_regression(preprocessor, X_train, y_train):

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", LinearRegression())
    ])

    pipeline.fit(X_train, y_train)

    return pipeline


def train_decision_tree(preprocessor, X_train, y_train):

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", DecisionTreeRegressor(random_state=42))
    ])

    pipeline.fit(X_train, y_train)

    return pipeline


def train_random_forest(preprocessor, X_train, y_train):

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ])

    pipeline.fit(X_train, y_train)

    return pipeline