# Customer Churn Prediction & Revenue Protection Strategy

This capstone project performs an end-to-end business data analysis to understand customer churn behavior and build a predictive machine learning model that identifies customers at high risk of leaving.

The goal is to help businesses reduce churn rate, protect recurring revenue, and implement proactive retention strategies using data-driven insights.

The project follows a complete analytics workflow including data cleaning, exploratory data analysis (EDA), statistical testing, machine learning modeling, and business recommendations.

# Project Overview

Customer churn is a major challenge for subscription-based businesses because losing customers increases customer acquisition costs and reduces long-term revenue.

This project builds a predictive churn model that allows organizations to:

- Identify customers likely to churn
- Prioritize retention campaigns
- Reduce revenue loss
- Improve long-term customer lifetime value

# Business Problem

The organization currently lacks a predictive system to detect customers who are likely to churn. Retention efforts are reactive rather than proactive, resulting in unnecessary revenue loss and inefficient marketing spending.

By analyzing historical customer data and building a churn prediction model, the business can identify high-risk customers early and apply targeted retention strategies.

# Dataset Overview

**Dataset Name:** `customer_churn.csv`

|    Attribute   | Details |
|----------------|---------|
|      Rows      |   500   |
|    Features    |    9    |
|Target Variable |  Churn  |

**Target Encoding**

- `0` → Customer Retained  
- `1` → Customer Churned  

### Key Variables

- Tenure
- MonthlyCharges
- TotalCharges
- Contract
- PaymentMethod
- PaperlessBilling
- SeniorCitizen

# Setup Instructions

### Clone Repository

```bash

git clone https://github.com/Dhanashree03-c/DataScienceProjects
cd Capstone_Project-Real_World_Business_Analysis_week8

### Create a Virtual Environment
python -m venv venv
```

Activate the environment.

### Windows
```bash
venv\Scripts\activate
```

### Mac / Linux
```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Analysis Notebook

```bash
jupyter notebook capstone_analysis.ipynb
```

# Technical Implementation

## Data Processing

Data preprocessing steps include:

- Missing value imputation
- Data type conversion
- Duplicate removal
- Feature engineering

### Engineered Feature

**AvgMonthlySpend**

```python
AvgMonthlySpend = TotalCharges / (Tenure + 1)
```

This feature helps capture **customer spending behavior over time.**

# Exploratory Data Analysis (EDA)

EDA was performed to identify patterns and relationships between customer attributes and churn.

Key visualizations include:

- Correlation heatmap
- Contract vs Churn distribution
- Tenure distribution
- Monthly charges analysis
- Feature importance visualization

# Statistical Analysis

To validate relationships between variables and churn, the following statistical tests were performed.

## Independent T-Test

Comparison of **Tenure between churned and retained customers**

**Result**
p-value = 2.43e-34

This indicates a **statistically significant difference in tenure.**

## Chi-Square Test

Relationship between **Contract type and Churn**

**Result**
p-value = 9.58e-07

This confirms **contract type significantly affects churn probability.**

# Machine Learning Models

Two models were implemented and evaluated.

## Logistic Regression

Used as a **baseline model**.

Evaluation method:

- 5-fold cross-validation
- ROC-AUC scoring

**Result**
Cross-Validation ROC-AUC = 0.9787

## Random Forest Classifier

Used as the **primary predictive model**.

Hyperparameter tuning performed using **GridSearchCV**.

**Best Parameters**
n_estimators = 100
max_depth = 5

# Model Performance

Model evaluated using a **hold-out test dataset**.

|      Metric       | Score |
|-------------------|-------|
| Accuracy          |  95%  |
| ROC-AUC           | 0.992 |
| Precision (Churn) | 1.00  |
| Recall (Churn)    | 0.69  |

The model demonstrates **excellent predictive performance and strong discrimination ability.**

# Key Insights

Important drivers of churn include:

- Short customer tenure
- Month-to-month contracts
- Higher monthly charges
- Certain payment methods

Customers with these characteristics show **significantly higher churn risk.**

# Revenue Impact Analysis

Using churn probability predictions, **high-risk customers were identified.**

Customers with **churn probability > 0.6** were classified as high risk.

**Estimated annual revenue loss**
Estimated Revenue at Risk = 10,212

A **customer risk scoring file** was generated for operational use.

**Output file**
data/customer_risk_scores.csv

This file can be integrated into **CRM systems to prioritize retention actions.**

# Business Recommendations

Based on the analysis, the following strategies are recommended:

- Convert month-to-month contracts to annual contracts
- Launch early engagement programs for new customers
- Offer loyalty discounts to high-spending customers
- Deploy automated churn scoring inside CRM platforms

Implementing these strategies can **significantly reduce churn and protect recurring revenue.**

# Testing & Validation

Validation checks included:

- Dataset size verification (≥500 rows)
- Missing value validation
- Statistical significance testing
- Cross-validation consistency
- Model evaluation on unseen test data

These checks ensure the **reliability and robustness of the analysis.**

# Future Improvements

Potential enhancements for production deployment:

- Deploy model as REST API using Flask or FastAPI
- Implement automated churn monitoring pipeline
- Add SHAP explainability for model interpretation
- Integrate real-time scoring with CRM systems
- Develop interactive dashboards using Power BI or Tableau