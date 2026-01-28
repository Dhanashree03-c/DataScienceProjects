# Sales Data Analysis using Python & Pandas

## Project Overview
This project performs exploratory data analysis and business metric evaluation on a sales dataset using **Python** and **pandas**. The goal is to clean raw sales data, compute key performance indicators (KPIs), and generate a structured sales report.

---

## Objectives
- Load and analyze sales data from a CSV file
- Clean and preprocess raw data
- Calculate important business metrics such as total revenue and best-selling products
- Identify top-performing regions
- Generate a clean and formatted sales report

## Technologies Used
- **Python 3**
- **pandas**

## Dataset Description
The dataset contains **100 sales records** with the following fields:

| Column Name  | Description                |
|--------------|----------------------------|
| Date         | Date of sale               |
| Product      | Product name               |
| Quantity     | Units sold                 |
| Price        | Price per unit             |
| Customer_ID  | Unique customer identifier |
| Region       | Sales region               |
| Total_Sales  | Revenue per transaction    |

---

## Data Cleaning Steps
- Converted date column to `datetime` format
- Removed duplicate records
- Handled missing values in numeric columns
- Recalculated total sales to ensure data consistency

## Key Metrics & Results
- **Total Revenue:** ₹12,365,048.00  
- **Best-Selling Product:** Laptop  
- **Total Quantity Sold:** 478 units  
- **Average Order Value:** ₹123,650.48  
- **Top-Performing Region:** North  

## How to Run the Project

### Install Dependencies
In terminal,
    pip install -r requirements.txt

### Install Dependencies
    python sales_analysis.py

