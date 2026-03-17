# Customer Churn Prediction - Data Preprocessing Report

## 1. Project Objective

The objective of this project is to preprocess customer data and engineer meaningful features to accurately predict customer churn. Churn prediction helps businesses identify at-risk customers and take proactive retention actions.

## 2. Dataset Overview

- Total Records: 500
- Features:
  - CustomerID
  - Tenure
  - MonthlyCharges
  - TotalCharges
  - Contract
  - PaymentMethod
  - PaperlessBilling
  - SeniorCitizen
  - Churn (Target Variable)

## 3. Data Exploration Insights

### 3.1 Churn Distribution

- Majority class: Non-churn (0)
- Minority class: Churn (1)

This indicates **class imbalance**, which can impact model performance.

### 3.2 Key Business Insights

#### Average Monthly Charges

| Churn|Avg Monthly Charges|
|------|-------------------|
| 0    | 111.72            |
| 1    | 129.77            |

Customers who churn tend to have **higher monthly charges**.

#### Average Tenure

|Churn | Avg Tenure|
|------|-----------|
| 0    | 40.15     |
| 1    | 6.00      |

Customers with **low tenure are significantly more likely to churn**.

#### Contract Type vs Churn

| Contract Type  | Non-Churn| Churn |
|----------------|----------|-------|
| Month-to-month | 79.4%    | 20.6% |
| One year       | 95.7%    | 4.3%  |
| Two year       | 93.0%    | 6.9%  |

Month-to-month contracts show **highest churn risk**.

## 4. Data Preprocessing Steps

### 4.1 Handling Categorical Variables

Three encoding techniques were applied:

1. **Label Encoding**
   - Used for binary categorical features
   - Example: PaperlessBilling

2. **One-Hot Encoding**
   - Used for multi-class categorical features
   - Example: Contract types

3. **Binary Encoding (Custom)**
   - Applied on PaymentMethod
   - Simplified into churn-relevant binary feature

### 4.2 Feature Scaling

Two scaling techniques were implemented and compared:

| Scaler           | Accuracy |
|------------------|----------|
| StandardScaler   | 0.98     |
| MinMaxScaler     | 0.98     |

Both scalers performed equally well, indicating the model is robust to scaling variations.

### 4.3 Outlier Detection

Two methods were used:

- **IQR Method**
- **Z-score Method**

Results:

- IQR Outliers: 0
- Z-score Outliers: 0

Dataset is clean with **no significant outliers detected**.

## 5. Feature Engineering

New features were created to improve model performance:

1. Customer Lifetime Value
2. Average Revenue per Month
3. Payment Efficiency
4. Senior Citizen × Contract Interaction
5. Charge Difference

These features help capture **customer behavior patterns and financial consistency**.

## 6. Feature Importance Analysis

Key findings:

- **Tenure** is the most important feature (~64% importance)
- MonthlyCharges and TotalCharges also contribute significantly
- Contract type impacts churn prediction

Business Insight:
Long-term customers are **far less likely to churn**, making tenure the most critical feature.

## 7. Model Performance

### 7.1 Hyperparameter Optimization

Best Parameters:{
'max_depth': 4,
'min_samples_leaf': 2,
'min_samples_split': 5,
'n_estimators': 200
}

### 7.2 Cross Validation

- Scores: [0.9922, 1.0, 0.9847, 0.9836, 1.0]
- Mean ROC-AUC: **0.9921**

Model shows **excellent generalization performance**.

### 7.3 Test Performance

#### Accuracy

- Training: 97%
- Testing: 96%

### 7.4 Classification Report

|Class | Precision| Recall | F1-score |
|------|----------|--------|----------|
| 0    | 1.00     | 0.96   | 0.98     |
| 1    | 0.73     | 1.00   | 0.85     |

The model:
- Perfectly identifies most churners (**recall = 1.00**)
- Slightly lower precision → some false positives

### 7.5 Confusion Matrix Insights

- Very low false negatives (important for churn use-case)
- Some false positives (acceptable in business context)

Business Impact:
Better to **flag extra customers** than miss actual churners.

## 8. Pipeline Implementation

A complete preprocessing pipeline was built using:

- ColumnTransformer
- StandardScaler
- RandomForestClassifier

This ensures:

- Reproducibility
- Scalability
- Clean workflow

## 9. Key Strengths

✔ Multiple encoding techniques implemented
✔ Two scaling techniques compared
✔ No data leakage observed
✔ Strong feature engineering
✔ High model performance (ROC-AUC ~0.99)
✔ Clean pipeline architecture

## 10. Limitations

- Small dataset (500 rows)
- Class imbalance not explicitly handled (e.g., SMOTE)
- Limited categorical diversity

## 11. Future Improvements

- Apply SMOTE for class imbalance
- Try advanced models (XGBoost, LightGBM)
- Perform feature selection using SHAP values
- Deploy model using Flask or FastAPI

## 12. Conclusion

The preprocessing pipeline successfully transforms raw customer data into a structured format suitable for machine learning.

Key findings:

- **Tenure is the strongest predictor of churn**
- **Short-term customers are high-risk**
- **Higher monthly charges increase churn probability**

The final model achieves:

- Accuracy: ~96–97%
- ROC-AUC: ~0.99

This demonstrates a **highly effective churn prediction system**.