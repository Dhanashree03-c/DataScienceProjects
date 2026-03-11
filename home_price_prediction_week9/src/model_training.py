"""
Model Training Module
Contains functions to train ML models
"""

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def train_linear_regression(preprocessor, X_train, y_train):
    """
    Train Linear Regression model.
    """

    model = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("model", LinearRegression())
    ])

    model.fit(X_train, y_train)

    return model


def train_decision_tree(preprocessor, X_train, y_train):
    """
    Train Decision Tree Regressor.
    """

    model = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("model", DecisionTreeRegressor(random_state=42))
    ])

    model.fit(X_train, y_train)

    return model


def train_random_forest(preprocessor, X_train, y_train):
    """
    Train Random Forest Regressor.
    """

    model = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("model", RandomForestRegressor(
            n_estimators=100,
            random_state=42
        ))
    ])

    model.fit(X_train, y_train)

    return model