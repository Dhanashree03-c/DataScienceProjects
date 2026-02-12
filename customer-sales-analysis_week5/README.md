# Customer Sales Analysis Project

## Overview

This project performs an end-to-end analysis of customer purchasing behavior by integrating sales transaction data with customer churn information. The goal is to uncover business insights such as top customers, regional performance, product trends, customer retention, and cross-selling opportunities.

The analysis is implemented using Python and Pandas, following industry best practices for data cleaning, feature engineering, aggregation, visualization, and reporting.


## Objectives

- Analyze customer purchasing patterns
- Identify top customers based on Lifetime Value
- Evaluate sales performance by region, product, and month
- Measure customer churn and retention
- Discover cross-selling opportunities
- Build visual dashboards for business decision-making

## Datasets

### Sales Data (`sales_data.csv`)
- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

### Customer Data (`customer_churn.csv`)
- CustomerID
- Tenure
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- PaperlessBilling
- SeniorCitizen
- Churn

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Key Features

### Data Cleaning & Preparation
- Converted date formats
- Handled missing values
- Standardized customer IDs
- Feature engineering (Month, Lifetime Value)

### Data Integration
- Merged sales and churn datasets using customer identifiers

### Aggregations
- Revenue by region
- Monthly sales trends
- Product-wise performance

### Pivot Tables
- Sales summarized by Region and Product

### Customer Analysis
- Lifetime Value calculation
- Top customer identification
- Churn rate estimation

### Cross-Selling Analysis
- Customer-product purchase matrix
- Product correlation analysis

### Visualization Dashboard
- Revenue by Region
- Monthly Sales Trend
- Top Products
- Churn Distribution
- Customer Lifetime Value Distribution

## Sample Metrics

- Total Revenue
- Total Customers
- Average Order Value
- Top Customer by Lifetime Value
- Customer Churn Rate

## Business Insights

- East region generates highest revenue
- Phones are the best-selling product
- Month-to-month customers exhibit higher churn
- High lifetime customers generally have longer tenure
- Phone and Headphones show strong cross-selling potential

## How to Run

1. Clone the repository

https://github.com/Dhanashree03-c/DataScienceProjects.git

2. Navigate to the file folder

customer-sales-analysis_week5

3. Run the command in terminal

python notebook
