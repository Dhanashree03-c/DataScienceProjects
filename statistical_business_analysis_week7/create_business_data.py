"""
This script:
1. Loads customer_churn.csv and sales_data.csv
2. Cleans and preprocesses data
3. Engineers revenue features
4. Standardizes Customer IDs
5. Aggregates customer-level metrics
6. Merges datasets correctly
7. Saves business_data.csv
"""

# IMPORT LIBRARIES
import pandas as pd
import numpy as np
from pathlib import Path

# DEFINE FILE PATHS
DATA_PATH = Path("data")
CHURN_FILE = DATA_PATH / "customer_churn.csv"
SALES_FILE = DATA_PATH / "sales_data.csv"
OUTPUT_FILE = DATA_PATH / "business_data.csv"

# LOAD DATASETS
print("Loading datasets...")

churn_df = pd.read_csv(CHURN_FILE)
sales_df = pd.read_csv(SALES_FILE)

print("Datasets loaded successfully.\n")

# DATA CLEANING - CHURN DATA
print("Cleaning customer churn dataset...")

# Convert numeric columns
churn_df["TotalCharges"] = pd.to_numeric(
    churn_df["TotalCharges"], errors="coerce"
)
churn_df["MonthlyCharges"] = pd.to_numeric(
    churn_df["MonthlyCharges"], errors="coerce"
)

# Fill missing numeric values with median
numeric_cols = churn_df.select_dtypes(include=np.number).columns
churn_df[numeric_cols] = churn_df[numeric_cols].fillna(
    churn_df[numeric_cols].median()
)

# Remove duplicate customers
churn_df = churn_df.drop_duplicates(subset="CustomerID")

print("Churn dataset cleaned.\n")

# DATA CLEANING - SALES DATA
print("Cleaning sales dataset...")

sales_df["Date"] = pd.to_datetime(
    sales_df["Date"], dayfirst=True, errors="coerce"
)

sales_df["Quantity"] = pd.to_numeric(sales_df["Quantity"], errors="coerce")
sales_df["Price"] = pd.to_numeric(sales_df["Price"], errors="coerce")

sales_df.dropna(subset=["Quantity", "Price"], inplace=True)
sales_df = sales_df.drop_duplicates()

print("Sales dataset cleaned.\n")

# FEATURE ENGINEERING
print("Creating revenue features...")

sales_df["Revenue"] = sales_df["Quantity"] * sales_df["Price"]

# STANDARDIZE CUSTOMER IDS
print("Standardizing Customer IDs for correct merging...")

# Extract numeric part from IDs
churn_df["Customer_Num"] = churn_df["CustomerID"].str.extract(r'(\d+)').astype(int)
sales_df["Customer_Num"] = sales_df["Customer_ID"].str.extract(r'(\d+)').astype(int)

print("Customer ID standardization completed.\n")

# AGGREGATE CUSTOMER-LEVEL SALES METRICS
print("Aggregating sales by customer...")

customer_sales = (
    sales_df.groupby("Customer_Num")
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Avg_Transaction_Value=("Revenue", "mean"),
        Total_Quantity=("Quantity", "sum"),
        Avg_Quantity=("Quantity", "mean"),
        Purchase_Frequency=("Date", "count"),
    )
    .reset_index()
)

print("Customer-level aggregation completed.\n")

# MERGE CHURN + SALES DATA
print("Merging datasets...")

business_df = pd.merge(
    churn_df,
    customer_sales,
    on="Customer_Num",
    how="left"
)

# Drop helper column
business_df.drop(columns=["Customer_Num"], inplace=True)

# Fill customers without purchases
sales_columns = [
    "Total_Revenue",
    "Avg_Transaction_Value",
    "Total_Quantity",
    "Avg_Quantity",
    "Purchase_Frequency"
]

business_df[sales_columns] = business_df[sales_columns].fillna(0)

print("Datasets merged successfully.\n")

# FINAL VALIDATION
print("Final dataset shape:", business_df.shape)

print("\nSales Columns Summary (Should NOT be all zeros):")
print(business_df[sales_columns].sum())

print("\nMissing values check:")
print(business_df.isnull().sum())

# SAVE BUSINESS_DATA.CSV
business_df.to_csv(OUTPUT_FILE, index=False)

print(f"\nbusiness_data.csv created successfully at: {OUTPUT_FILE}")