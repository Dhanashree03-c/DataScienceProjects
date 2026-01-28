import pandas as pd
from typing import Tuple

#Configuration
#to keep important data paths and formats in one place
DATA_PATH = 'sales_data.csv'
DATE_FORMAT = '%d-%m-%Y'

#Utility Functions
def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)    #read csv file and return dataframe

#to ensure data integrity before analysis
def validate_columns(df: pd.DataFrame) -> None:
    required_columns  = {"Date", "Product", "Quantity", "Price", "Customer_ID", "Region", "Total_Sales"}
    
    missing = required_columns - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    
    df = df.copy()   #prevent modifying original dataframe
    
    #convert date column to datetime format making invalid parsing to NaT
    df["Date"] = pd.to_datetime(df["Date"], format = DATE_FORMAT, errors = "coerce")
    df.drop_duplicates(inplace = True)  #prevent double counting sales
    
    numeric_columns = ["Quantity", "Price"]
    df[numeric_columns] = df[numeric_columns].fillna(0) #fill missing numeric values with 0
    
    #convert text to numeric, invalid parsing to NaN then fill NaN with 0
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors = "coerce").fillna(0)
    
    #ensure accurate revenue calculation even if original data is incorrect
    df["Total_Sales"] = df["Quantity"] * df["Price"]
    
    return df

#computing business metrics
def analyze_sales(df: pd.DataFrame) -> Tuple[float, str, int, float, str]:
    """
    Perform sales analysis and return key metrics.
    Returns:
        - Total Revenue
        - Best Selling Product
        - Total Quantity Sold
        - Average Order Value
        - Top-performing Region
    """
    total_revenue = df["Total_Sales"].sum()
    
    best_selling_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
    
    total_quantity = int(df["Quantity"].sum())
    
    avg_order_val = df["Total_Sales"].mean()
    
    top_region = df.groupby("Region")["Total_Sales"].sum().idxmax()
    
    return (total_revenue, best_selling_product, total_quantity, avg_order_val, top_region)


#print formatted report
def print_report(
    total_revenue: float,
    best_selling_product: str,
    total_quantity: int,
    avg_order_val: float,
    top_region: str
) -> None:
    
    print("\n" + "-" * 15 + "Sales Report" + "-" * 15)
    print(f"\nTotal Revenue: ₹{total_revenue:,.2f}")
    print(f"\nBest Selling Product: {best_selling_product}")
    print(f"\nTotal Quantity Sold: {total_quantity}")
    print(f"\nAverage Order Value: ₹{avg_order_val:,.2f}")
    print(f"\nTop-performing Region: {top_region}")
    print("\n" + "-" * 42)

#Main Execution
def main() -> None:
    
    df = load_data(DATA_PATH)
    
    print(f"\nData Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nData Types: {df.dtypes}")
    
    validate_columns(df)
    
    df = clean_data(df)
    
    metrics = analyze_sales(df)
    
    print_report(*metrics)
    
if __name__ == "__main__":
    main()