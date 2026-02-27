# Statistical Business Analysis Project

This project performs a statistical analysis of business and customer data to uncover revenue trends, customer behavior, and contract/tenure patterns. Using Python and Pandas, it applies descriptive statistics, hypothesis testing, correlation analysis, confidence intervals, and regression modeling to generate actionable business insights for data-driven decision-making.

## 1. Dataset
The analysis uses `business_data.csv`, which combines customer churn data and sales data with the following key columns:
- `CustomerID`, `Tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `PaperlessBilling`, `SeniorCitizen`, `Churn`
- `Total_Revenue`, `Avg_Transaction_Value`, `Total_Quantity`, `Avg_Quantity`, `Purchase_Frequency`

## 2. Setup and Installation Instructions
**Prerequisites:**
- Python 3.10+
- Jupyter Notebook

**Installation Steps:**
1. Download or clone the project repository from GitHub.
2. Install required libraries:
    ```bash
    pip install -r requirements.txt
3. Run in terminal:
    python notebook

## 3. Key Analysis Performed
- Descriptive Statistics: Mean, median, standard deviation, and quartiles for numeric columns.
- Distribution Analysis: Histogram and KDE plots to understand revenue distribution.
- Correlation Analysis: Heatmap and Pearson correlation to examine relationships between numeric variables.
## 4. Hypothesis Testing:
- Revenue difference between churned and non-churned customers
- MonthlyCharges differences across contract types (ANOVA)
- Revenue difference between senior and non-senior customers
- Confidence Interval: 95% confidence interval for average revenue.
- Regression Analysis: OLS regression of Total_Revenue on MonthlyCharges, Tenure, and SeniorCitizen.

## 4. Key Insights
- Total Revenue is right-skewed, with most customers generating lower revenue.
- Revenue is strongly correlated with MonthlyCharges.
- Customers with longer tenure contribute higher lifetime revenue.
- Contract type significantly impacts MonthlyCharges.
- Revenue difference between churned and retained customers is statistically significant.
- Regression model explains a meaningful portion of revenue variability, highlighting key predictors.