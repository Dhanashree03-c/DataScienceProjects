"""
Visualization Module
Functions for data visualization and model prediction plots
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_area_vs_price(data):
    """
    Scatter plot: Area vs Price
    """

    plt.figure(figsize=(8,6))

    sns.scatterplot(
        x="Area",
        y="Price",
        data=data
    )

    plt.title("Area vs House Price")

    plt.show()


def plot_location_vs_price(data):
    """
    Box plot: Location vs Price
    """

    plt.figure(figsize=(8,6))

    sns.boxplot(
        x="Location",
        y="Price",
        data=data
    )

    plt.title("Location vs Price")

    plt.show()


def plot_predictions_vs_actual(y_test, predictions, save_path):
    """
    Plot predicted vs actual house prices.
    """

    plt.figure(figsize=(8,6))

    plt.scatter(y_test, predictions)

    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")

    plt.title("Actual vs Predicted Prices")

    plt.plot(
        [y_test.min(), y_test.max()],
        [y_test.min(), y_test.max()]
    )

    plt.savefig(save_path)

    plt.show()