# Model Report — Customer Churn Prediction

Author: Dhanashree Tankar
Project: Customer Churn Prediction System
Date: 2026


# 1. Objective

The objective of this project is to build a machine learning model that predicts whether a telecom customer is likely to churn based on behavioral, demographic, and subscription-related features.

Early identification of high-risk customers allows businesses to implement targeted retention strategies and reduce revenue loss.

# 2. Dataset Summary

Dataset Size: **500 customer records**

Key features include:

| Feature          | Description                                           |
| ---------------- | ----------------------------------------------------- |
| Tenure           | Number of months customer has stayed with the company |
| MonthlyCharges   | Monthly subscription fee                              |
| TotalCharges     | Total amount billed to the customer                   |
| Contract         | Contract type (Month-to-Month, One-Year, Two-Year)    |
| PaymentMethod    | Customer payment method                               |
| PaperlessBilling | Whether billing is paperless                          |
| SeniorCitizen    | Whether the customer is a senior citizen              |
| Churn            | Target variable (1 = churn, 0 = stay)                 |


# 3. Data Preprocessing

The following preprocessing steps were applied:

• Missing value validation
• Data type verification
• Encoding categorical variables
• Boolean to integer conversion
• Removal of non-informative features (e.g., CustomerID)

The processed dataset was saved for reproducibility.

# 4. Feature Engineering

Feature engineering included:

• Separation of feature matrix (X) and target variable (y)
• Removal of identifier columns
• Conversion of boolean features to numeric values

Final Feature Matrix Shape: **(500, N features)**

# 5. Model Development

Two machine learning algorithms were evaluated:

### Logistic Regression

A baseline linear classification model used for comparison.

### Random Forest Classifier

An ensemble learning algorithm that constructs multiple decision trees and aggregates predictions for improved performance.

Pipelines were used to standardize preprocessing and model training.

# 6. Model Evaluation

Models were evaluated using the following metrics:

• Accuracy
• ROC-AUC Score
• Precision
• Recall
• Confusion Matrix

These metrics provide a comprehensive view of classification performance.

# 7. Final Model Selection

The **Random Forest Classifier** was selected as the final model due to superior predictive performance.

### Performance Metrics

| Metric            | Score    |
| ----------------- | -------- |
| Accuracy          | **0.96** |
| ROC-AUC           | **0.99** |
| Precision (Churn) | High     |
| Recall (Churn)    | 0.64     |

The high ROC-AUC score indicates strong separation between churn and non-churn customers.

# 8. Feature Importance

Random Forest feature importance analysis revealed the most influential predictors:

1. Tenure
2. MonthlyCharges
3. TotalCharges
4. Contract Type
5. Payment Method

These features significantly influence customer churn behavior.

# 9. High-Risk Customer Identification

The model calculates **churn probability scores** for each customer.

Customers with the highest predicted probabilities are flagged as **high-risk**, enabling proactive retention strategies.

Example output includes a ranked list of customers based on churn risk.

# 10. Business Insights

Key insights derived from the analysis:

• Customers with **short tenure** are significantly more likely to churn
• **Month-to-month contracts** have the highest churn rates
• Higher **monthly charges** correlate with increased churn probability
• Customers with **long tenure exhibit strong loyalty**

# 11. Business Recommendations

Based on model findings, the following strategies are recommended:

1. Encourage customers to shift from **month-to-month to long-term contracts**
2. Implement **customer engagement programs during the first 6–12 months**
3. Offer **targeted retention discounts for high-risk customers**
4. Monitor churn probabilities and trigger **automated retention campaigns**

# 12. Deployment

The trained model was serialized using **pickle** and saved as:

```
deployment/model.pkl
```

This model can be integrated into production systems or APIs to perform real-time churn predictions.

# 13. Limitations

• Dataset size is relatively small (500 records)
• Recall for churn class can be improved
• Additional behavioral features could further enhance model performance

# 14. Future Improvements

Possible enhancements include:

• Larger and more diverse datasets
• Advanced models such as **XGBoost or LightGBM**
• Model monitoring and retraining pipeline
• Real-time churn prediction API deployment

# 15. Conclusion

This project demonstrates a complete end-to-end data science workflow, including data analysis, feature engineering, machine learning modeling, and evaluation.

The final Random Forest model achieved strong predictive performance with **96% accuracy and 0.99 ROC-AUC**, enabling telecom companies to identify high-risk customers and implement proactive retention strategies.
