## Objective
The objective of this project is to analyze a sales dataset to identify Total revenue, best-selling product and overall sales performance using python and pandas.

## Dataset Overview
- **Total Records:** 100
- **Total Columns:** 7
- **Key Fields:**
  - Date
  - Product
  - Quantity
  - Price
  - Customer_ID
  - Region
  - Total_Sales

## Data Preprocessing
The dataset was cleaned and prepared using the following steps:
- Converted the `Date` column to datetime format
- Removed duplicate records
- Handled missing values in numeric fields
- Recalculated `Total_Sales` to ensure accuracy

## Key Metrics Calculated
### 1. Total Revenue
- ₹12,365,048.00

### 2. Best-Selling Product
- Laptop

### 3. Total Quantity Sold
- 478 units

### 4. Average Order Value
- ₹123,650.48

### 5. Top-Performing Region
- North

## Insights
- Laptops are the primary revenue driver, indicating strong customer demand.
- The North region contributes the highest sales, making it a key market area.
- A high average order value suggests customers tend to purchase premium or multiple items per transaction.

## Conclusion
This analysis demonstrates how pandas can be used to efficiently clean, analyze and extract business insights from sales data.