"""
Model Evaluation Module

This module contains helper functions used to evaluate the
performance of regression models. It calculates common
evaluation metrics used in machine learning regression tasks.
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_regression(y_true, y_pred):
    """
    Calculate common regression evaluation metrics.
    """

    #Mean Absolute Error: Average absolute difference between predicted and actual values
    mae = mean_absolute_error(y_true, y_pred)
    
    #Mean Squared Error: Average of squared differences between predictions and actual values
    mse = mean_squared_error(y_true, y_pred)
    
    #Root Mean Squared Error: Square root of MSE, provides error in same unit as target variable
    rmse = np.sqrt(mse)
    
    #R-squared Score: Measures how well the model explains variance in the data
    r2 = r2_score(y_true, y_pred)

    #Return metrics as dictionary for easy reuse
    return {  
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "R2": r2
    }

def print_metrics(model_name, metrics):
    #Display evaluation metrics in a readable format.
    print(f"\nModel: {model_name}")  #Print model name as a header
    print("-" * 30)                  #Separator for better readability

    #Iterate through each metric and display its value
    for metric, value in metrics.items():
        print(f"{metric}: {value:,.2f}")