"""
Contains all statistical visualizations built using Seaborn.
All plot are saved into outputs/ directory.
"""

import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

OUTPUT_DIR = "outputs"

def _ensure_output_dir() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True) #prevents file saving errors during execution
    
def save_plot(fig, filename: str):
    _ensure_output_dir()
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    #Save figure with high resolution for professional presentation
    fig.savefig(filepath, dpi=300, bbox_inches="tight")
    #Close figure to free memory
    plt.close(fig)
    return filepath

def box_price_distribution(df: pd.DataFrame) -> str:
    fig, ax = plt.subplots()
    sns.boxplot(x = "Product", y = "Price", data = df, ax = ax)
    ax.set_title("Price Distribution by Product")
    ax.tick_params(axis = "x", rotation = 30)
    return save_plot(fig, "box_price_distribution.png")
    
def violin_quantity_distribution(df: pd.DataFrame) -> str:
    fig, ax = plt.subplots()
    sns.violinplot(x = "Product", y = "Quantity", data = df, ax = ax)
    ax.set_title("Quantity Distribution by Product")
    ax.tick_params(axis = "x", rotation = 30)
    return save_plot(fig, "violin_quantity_distribution.png")
    
def correlation_heatmap(df: pd.DataFrame) -> str | None:
    numeric_df = df.select_dtypes(include="number") #Select only numeric columns

    if numeric_df.shape[1] < 2: #Require at least 2 numeric columns to compute correlation
        return None

    correlation = numeric_df.corr()

    #Safety check: ensure correlation matrix is not empty
    if correlation.empty:
        return None

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        ax=ax
    )
    ax.set_title("Correlation Heatmap")

    return save_plot(fig, "correlation_heatmap.png")
    
def sales_by_region(df: pd.DataFrame) -> str:
    #Aggregate total sales by region
    region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()
    
    fig, ax = plt.subplots()
    sns.barplot(data = region_sales, x = "Region", y = "Total_Sales", ax = ax)
    ax.set_title("Total Sales by Region")
    return save_plot(fig, "sales_by_region.png")