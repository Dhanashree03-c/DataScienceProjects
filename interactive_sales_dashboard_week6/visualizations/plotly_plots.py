"""
Contains interactive visualizations built using Plotly.
"""

import plotly.express as px
import pandas as pd
from plotly.graph_objs import Figure

def sales_trend(df: pd.DataFrame) -> Figure:
    #aggregate total sales at daily level
    daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()

    #Create interactive line chart
    fig = px.line(
        daily_sales,
        x="Date",
        y="Total_Sales",
        markers = True,       #adds circular markers for better visibility
        title="Daily Sales Trend",
        template = "plotly_white"
    )
    
    #improve layout aesthetics
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales",
        hovermode="x unified"  #single tooltip across vertical axis
    )

    return fig


def product_performance(df: pd.DataFrame) -> Figure:
    #Compute total revenue per product
    product_sales = (df.groupby("Product")["Total_Sales"].sum().reset_index())

    fig = px.bar(
        product_sales,
        x="Product",
        y="Total_Sales",
        color="Product",     #color differentiation per category
        title="Product Performance",
        template = "plotly_white"
    )
    
    #improve readability
    fig.update_layout(
        xaxis_title="Product",
        yaxis_title="Total Revenue",
        showlegend=False
    )

    return fig


def customer_segmentation(df: pd.DataFrame) -> Figure:
    #Aggregate customer-level metrics
    customer_sales = (
        df.groupby("Customer_ID")
        .agg({
            "Total_Sales": "sum",
            "Quantity": "sum"
        }).reset_index()
    )

    fig = px.scatter(
        customer_sales,
        x="Quantity",
        y="Total_Sales",
        hover_data=["Customer_ID"],  #shoe customer ID on hover
        title="Customer Segmentation (Quantity vs Total Sales)",
        template = "plotly_white"
    )
    
    #enhance visual clarity
    fig.update_layout(
        xaxis_title="Total Quantity Purchased",
        yaxis_title="Total Revenue Generated",
        hovermode="closest"
    )

    return fig