# Customer Churn Prediction – Business Report

**Project:** Customer Churn Prediction System
**Author:** Dhanashree Tankar
**Date:** 2026

# 1. Executive Summary

Customer churn is a major challenge for subscription-based companies such as telecommunications providers. Losing customers directly impacts revenue and increases acquisition costs, as acquiring a new customer can cost significantly more than retaining an existing one.

This project developed a **machine learning-based churn prediction system** capable of identifying customers who are most likely to cancel their subscription. The model analyzes customer behavior, subscription details, and billing patterns to estimate churn probability.

The final model achieved **96% accuracy and a ROC-AUC score of 0.99**, demonstrating strong predictive capability. Using this system, businesses can proactively target high-risk customers with retention strategies, reducing churn and improving customer lifetime value.

# 2. Business Problem

Telecommunication companies face significant revenue loss due to customer churn. Without predictive systems, organizations typically react **after the customer has already left**.

Key challenges include:

* Difficulty identifying which customers are likely to leave
* Lack of proactive retention strategies
* High cost of acquiring replacement customers
* Limited visibility into behavioral patterns that lead to churn

A predictive analytics system can help businesses **identify churn risk early and implement targeted retention campaigns**.

# 3. Dataset Overview

The dataset contains **500 customer records** representing behavioral and subscription information.

Key variables include:

| Feature          | Description                                       |
| ---------------- | ------------------------------------------------- |
| Tenure           | Number of months the customer has been subscribed |
| MonthlyCharges   | Monthly service fee                               |
| TotalCharges     | Total amount billed to the customer               |
| Contract         | Type of subscription contract                     |
| PaymentMethod    | Payment method used                               |
| PaperlessBilling | Whether paperless billing is enabled              |
| SeniorCitizen    | Customer demographic indicator                    |
| Churn            | Target variable indicating if customer left       |

The dataset was cleaned, validated, and transformed before model training.

# 4. Analytical Approach

The project followed a structured data science workflow:

1. Data exploration and visualization
2. Data preprocessing and cleaning
3. Feature engineering
4. Model training and evaluation
5. Hyperparameter optimization
6. Business insight generation

Two machine learning algorithms were evaluated:

* Logistic Regression
* Random Forest Classifier

Random Forest produced the best predictive performance and was selected as the final model.

# 5. Model Performance

The final Random Forest model demonstrated strong classification performance.

| Metric    | Score    |
| --------- | -------- |
| Accuracy  | 96%      |
| ROC-AUC   | 0.99     |
| Precision | High     |
| Recall    | Moderate |

These results indicate that the model is **highly effective at identifying customers likely to churn**.

# 6. Key Business Insights

Data analysis revealed several behavioral patterns associated with customer churn.

### 1. New Customers Are Most At Risk

Customers with **short tenure** showed significantly higher churn rates. The first few months of service are critical for retention.

### 2. Higher Monthly Charges Increase Churn Probability

Customers paying **higher monthly fees** were more likely to cancel their subscriptions.

### 3. Contract Type Strongly Influences Retention

Customers with **month-to-month contracts** exhibited the highest churn rates, while long-term contracts reduced churn risk.

### 4. Long-Term Customers Are Highly Loyal

Customers with long tenure demonstrated strong retention and low churn probability.

### 5. High-Risk Customers Can Be Identified Early

The model successfully identified customers with **over 80% churn probability**, allowing targeted retention actions.

# 7. Business Recommendations

Based on the analysis and model insights, the following strategies are recommended:

### 1. Promote Long-Term Contracts

Offer incentives for customers to switch from month-to-month plans to annual or multi-year contracts.

### 2. Improve Early Customer Engagement

Develop onboarding programs and early support initiatives during the first **6–12 months** of subscription.

### 3. Provide Targeted Retention Offers

Offer personalized discounts or benefits to customers identified as high churn risk.

### 4. Monitor High Monthly Charge Segments

Customers paying higher fees should receive proactive engagement and value reinforcement.

### 5. Integrate Predictive Model into CRM Systems

The churn prediction model can be deployed within customer relationship management systems to automatically flag high-risk customers.

# 8. Business Impact

Implementing a churn prediction system can provide several advantages:

* Reduced customer attrition
* Increased customer lifetime value
* More efficient marketing and retention campaigns
* Data-driven decision making

Even a **5% reduction in churn can significantly increase company profitability**.

# 9. Conclusion

This project demonstrates the practical application of machine learning to solve a critical business problem.

The developed churn prediction system accurately identifies customers at risk of leaving and provides actionable insights for retention strategies.

By integrating predictive analytics into operational processes, organizations can **proactively reduce churn, strengthen customer relationships, and improve long-term revenue stability**.
