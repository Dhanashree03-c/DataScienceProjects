"""
Visualization utilities for data exploration and predictions.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_area_vs_price(data):

    plt.figure(figsize=(8,6))
    sns.scatterplot(x="Area", y="Price", data=data)
    plt.title("Area vs Price")
    plt.show()


def plot_location_vs_price(data):

    plt.figure(figsize=(8,6))
    sns.boxplot(x="Location", y="Price", data=data)
    plt.title("Location vs Price")
    plt.show()


def plot_predictions_vs_actual(y_true, y_pred, save_path):

    plt.figure(figsize=(8,6))

    plt.scatter(y_true, y_pred)

    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")

    plt.title("Actual vs Predicted House Prices")

    plt.plot(
        [y_true.min(), y_true.max()],
        [y_true.min(), y_true.max()],
        color="red"
    )

    plt.savefig(save_path)

    plt.show()