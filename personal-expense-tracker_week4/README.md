# Personal Expense Tracker

This project implements a complete end-to-end data analysis pipeline for personal expense tracking using Python.
The main goal is to analyze spending patterns, identify major expense categories, visualize monthly trends, and generate actionable insights from real-world financial data.

The system performs:
- Data loading and validation
- Data cleaning and preprocessing
- Feature engineering
- Statistical analysis
- Visualization using multiple chart types
- Automated report generation

## Dataset Description
The dataset containg **4,597 expenses records** with the following fields:

- 'date' - Transaction date
- 'category' - Expense category (Food, Bills, Shopping, etc.)
- 'amount' - Expense amount

## Dataset Source
The dataset was downloaded from Kaggle:
https://www.kaggle.com/datasets/ismetsemedov/personal-budget-transactions-dataset

The Kaggle dataset includes approximately **3,600+ expense records** with columns such as `date`, `category`, and `amount`.

The version used in this repository has been preprocessed and extended to ~4,597 records for thorough analysis.

The dataset file is stored locally as: data/expenses.csv

## Technologies Used
This project uses the following libraries:

- **Python 3.x**
- **Pandas** – Data manipulation and cleaning
- **NumPy** – Numerical operations
- **Matplotlib** – Visualization
- **Logging** – Pipeline traceability

## How to run
pip install -r requirements.txt
python main.py

## Visualization Generated
The following charts are generated and saved to visualizations/:
* Bar Chart - Expense by Category
* Pie Chart - Expense Distribution
* Line Chart - Monthly Expense Trend

## Report Output
The automated Markdown report includes:
- Summary statistics
- Category-wise spending breakdown
- Monthly trend table
- Key insights

Report saved in:
report/report.md

## Key Insights
- Categories like Bills, Food, and Shopping drive the largest portion of total expenses.
- Monthly expense trend shows spending variation over time.
- These insights can inform budgeting decisions and cost optimization.