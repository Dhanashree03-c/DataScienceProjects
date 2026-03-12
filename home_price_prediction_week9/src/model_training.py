"""
Model Training Module

This module contains reusable functions to train different
machine learning regression models for the house price prediction project.

Each function creates a pipeline that includes:
1. Data preprocessing
2. Model training

Using pipelines ensures that preprocessing steps are applied
consistently during both training and prediction.
"""

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

#Train a Linear Regression model.
def train_linear_regression(preprocessor, X_train, y_train):

    #Create pipeline with preprocessing and model
    pipeline = Pipeline([
        ("preprocessing", preprocessor), #Apply feature preprocessing
        ("model", LinearRegression())    #Linear Regression model
    ])

    #Train the model on training data
    pipeline.fit(X_train, y_train)

    #Return the trained pipeline
    return pipeline

def train_decision_tree(preprocessor, X_train, y_train):
    """
    Train a Decision Tree Regressor model.

    Decision Trees capture nonlinear relationships between
    input features and the target variable.
    """
    pipeline = Pipeline([
        ("preprocessing", preprocessor), #Feature preprocessing
        ("model", DecisionTreeRegressor(random_state=42)) #Decision Tree model
    ])

    #Train the decision tree model
    pipeline.fit(X_train, y_train)

    return pipeline


def train_random_forest(preprocessor, X_train, y_train):
    """
    Train a Random Forest Regressor model.

    Random Forest is an ensemble learning algorithm that builds
    multiple decision trees and averages their predictions.
    It generally performs better and is more robust than a single tree.
    """
    pipeline = Pipeline([
        ("preprocessing", preprocessor),  #Apply preprocessing
        ("model", RandomForestRegressor(  #Random Forest model
            n_estimators=100,             #number of trees
            random_state=42               #ensures reproducibility
        ))
    ])

    pipeline.fit(X_train, y_train)  #Train the random forest model

    return pipeline