# Customer Churn Prediction System

### End-to-End Data Science Capstone Project

Author: **Dhanashree Tankar**

# Project Overview

Customer churn is a critical challenge for subscription-based businesses such as telecommunications, SaaS platforms, and financial services. Losing customers directly impacts revenue and increases acquisition costs.

This project builds a **machine learning system that predicts customer churn** using behavioral and subscription data. By identifying high-risk customers in advance, companies can implement **proactive retention strategies**.

The project demonstrates a **complete end-to-end data science workflow**, including data preprocessing, feature engineering, model training, evaluation, and deployment preparation.


# Business Problem

Acquiring a new customer can cost **5–7 times more** than retaining an existing one. Therefore, predicting which customers are likely to churn allows companies to:

* Reduce customer attrition
* Improve retention campaigns
* Increase long-term revenue
* Optimize marketing strategies

This system predicts whether a customer will **churn (leave the service)** or **remain subscribed**.


# Dataset Description

The dataset contains **500 customer records** with features describing customer behavior and subscription details.

### Key Features

| Feature          | Description                                  |
| ---------------- | -------------------------------------------- |
| Tenure           | Number of months the customer has stayed     |
| MonthlyCharges   | Monthly subscription fee                     |
| TotalCharges     | Total amount billed                          |
| Contract         | Contract type (Month-to-month, yearly, etc.) |
| PaymentMethod    | Customer payment method                      |
| PaperlessBilling | Whether billing is paperless                 |
| SeniorCitizen    | Demographic indicator                        |
| Churn            | Target variable (1 = churn, 0 = stay)        |


# Project Objectives

* Perform **exploratory data analysis (EDA)** to understand churn patterns
* Build a **data preprocessing pipeline**
* Engineer predictive features
* Train and compare machine learning models
* Tune hyperparameters for optimal performance
* Evaluate model performance using classification metrics
* Generate **business insights for churn reduction**


# Technologies Used

* **Python**
* **Pandas & NumPy** – Data manipulation
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Machine learning models and pipelines
* **Jupyter Notebook** – Experimentation and analysis


# Machine Learning Models

The following models were implemented and compared:

### Logistic Regression

* Baseline classification model
* Interpretable and efficient

### Random Forest

* Ensemble model
* Handles nonlinear relationships and feature interactions
* Provided the **best performance**


# Model Performance

| Metric            | Score    |
| ----------------- | -------- |
| Accuracy          | **96%**  |
| ROC-AUC           | **0.99** |
| Precision (Churn) | High     |
| Recall (Churn)    | 0.64     |

The Random Forest model demonstrated **excellent classification performance** and strong predictive capability.


# Key Insights

Analysis of customer behavior revealed several important churn patterns:

* Customers with **short tenure churn more frequently**
* **Month-to-month contracts have the highest churn rate**
* Customers with **higher monthly charges are more likely to churn**
* **Long-tenure customers exhibit strong loyalty**
* High-risk customers with **>80% churn probability** can be identified


# Business Recommendations

Based on the model findings, companies can reduce churn through:

* Incentivizing **long-term contracts**
* Targeted engagement during the **first 6–12 months**
* Offering **personalized retention offers for high monthly charge customers**
* Using churn predictions to **trigger proactive retention campaigns**


# Example Prediction

The model can predict churn probability for a given customer:

```
Prediction: Churn
Churn Probability: 87.42%
```

This enables companies to **identify and intervene with high-risk customers before they leave**.


# How to Run the Project

### 1 Install Dependencies

```
pip install -r requirements.txt
```

### 2 Run the Notebook

```
jupyter notebook churn_prediction.ipynb
```

### 3 Train the Model

The training pipeline will:

* Load the dataset
* Preprocess the data
* Train machine learning models
* Evaluate performance
* Save the best model


# Future Improvements

Possible enhancements for this project include:

* Deploying the model using **Streamlit or FastAPI**
* Building a **real-time churn prediction dashboard**
* Applying **advanced models such as XGBoost or LightGBM**
* Using **larger real-world telecom datasets**


# Conclusion

This project demonstrates a **complete machine learning pipeline for customer churn prediction**, combining data analysis, feature engineering, and model optimization.

The final Random Forest model achieves **strong predictive performance** and provides valuable insights that can help businesses **improve customer retention and reduce churn**.
