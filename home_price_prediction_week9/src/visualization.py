"""
Visualization utilities for data exploration and model predictions.

This module contains reusable plotting functions used during
Exploratory Data Analysis (EDA) and model evaluation.
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_area_vs_price(data):
    """
    Create a scatter plot showing the relationship between
    house area and price.

    This visualization helps identify whether larger houses
    tend to have higher prices.
    """

    plt.figure(figsize=(8,6)) #Create figure with specified size
    
    #Scatter plot: Area on x-axis and Price on y-axis
    sns.scatterplot(x="Area", y="Price", data=data)
    
    #Add title to describe the plot
    plt.title("Area vs Price")
    plt.show()  #Display the plot


def plot_location_vs_price(data):
    """
    Create a box plot showing how house prices vary
    across different locations.

    Box plots help visualize:
    - median price
    - price distribution
    - outliers
    """
    
    plt.figure(figsize=(8,6)) #Create figure with specified size
    
    #Box plot comparing price distributions by location
    sns.boxplot(x="Location", y="Price", data=data)
    
    #Title describing the visualization
    plt.title("Location vs Price")
    plt.show()  #Display the plot

def plot_predictions_vs_actual(y_true, y_pred, save_path):
    """
    Plot predicted house prices vs actual house prices.

    This visualization helps evaluate how well the model
    performs. Ideally, points should lie close to the
    diagonal line (perfect prediction).
    """
    plt.figure(figsize=(8,6))  #Create figure

    plt.scatter(y_true, y_pred) #Scatter plot of actual vs predicted values

    plt.xlabel("Actual Prices")  #Label x-axis
    plt.ylabel("Predicted Prices") #Label y-axis

    #Title describing the plot
    plt.title("Actual vs Predicted House Prices")

    #Plot a diagonal reference line showing perfect predictions
    plt.plot(
        [y_true.min(), y_true.max()],
        [y_true.min(), y_true.max()],
        color="red"
    )

    #Save the figure to the specified file path
    plt.savefig(save_path)

    plt.show() #Display the plot