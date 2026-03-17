# Feature Engineering Documentation  
## Customer Churn Prediction Project

---

## 1. Objective

The goal of feature engineering in this project is to transform raw customer data into meaningful features that improve model performance and capture underlying customer behavior patterns related to churn.

Feature engineering helps:
- Enhance predictive power
- Reveal hidden relationships in data
- Improve model interpretability
- Align technical features with business insights

---

## 2. Approach

Feature engineering was implemented using a **custom transformer (`FeatureEngineer`)** inside a machine learning pipeline to ensure:

- Reproducibility
- No data leakage during inference
- Compatibility with model deployment (joblib)
- Consistent transformation across training and testing

---

## 3. Engineered Features

### 3.1 CustomerLifetimeValue (CLV)

**Formula:** CustomerLifetimeValue = Tenure × MonthlyCharges


**Business Meaning:**
- Represents total revenue contributed by a customer over time
- High CLV customers are valuable and should be retained

**Impact:**
- Helps model identify high-value customers at risk of churn

---

### 3.2 AvgRevenuePerMonth

**Formula:** AvgRevenuePerMonth = TotalCharges / (Tenure + 1)


**Why +1?**
- Prevents division by zero for new customers

**Business Meaning:**
- Measures consistency of customer spending
- Detects irregular billing patterns

---

### 3.3 PaymentEfficiency

**Formula:** PaymentEfficiency = TotalCharges / MonthlyCharges


**Business Meaning:**
- Indicates how consistently a customer pays over time
- Low efficiency may indicate payment issues or dissatisfaction

---

### 3.4 SeniorCitizenContract Interaction

**Formula:** SeniorCitizenContract = SeniorCitizen × Contract_Type


**Business Meaning:**
- Captures interaction between age group and contract type
- Helps model detect behavioral differences in senior customers

---

### 3.5 ChargeDifference

**Formula:** ChargeDifference = TotalCharges − (MonthlyCharges × Tenure)


**Business Meaning:**
- Measures deviation from expected billing
- Highlights billing inconsistencies or discounts

---

## 4. Why These Features Matter

The engineered features capture **three key behavioral dimensions**:

### 4.1 Customer Value
- CustomerLifetimeValue
- AvgRevenuePerMonth

👉 Identifies high-value customers likely to churn

---

### 4.2 Payment Behavior
- PaymentEfficiency

👉 Detects irregular or risky payment patterns

---

### 4.3 Billing Consistency
- ChargeDifference

👉 Identifies anomalies in billing that may cause dissatisfaction

---

### 4.4 Demographic Interaction
- SeniorCitizenContract

👉 Captures combined effects not visible in individual features


## Key Advantages

- Integrated inside pipeline → prevents data leakage
- Automatically applied during:
  - Training
  - Testing
  - Inference
- Ensures consistent feature generation

## 5. Integration in Pipeline

Feature engineering is applied before preprocessing:

**Pipeline Flow:** FeatureEngineering → Encoding → Scaling → Model

### This ensures:

- New features are also scaled and encoded correctly
- No mismatch between training and prediction phases

## 6. Impact on Model Performance

### Observations:

- High ROC-AUC (~0.99)
- Strong recall for churn class (1.00)
- Feature importance dominated by:
  - Tenure
  - MonthlyCharges
  - Engineered financial features

Feature engineering contributed to improved separability between churn and non-churn customers.

## 7. Feature Importance Insights

- Tenure is the most dominant feature (~65%)
- Engineered features provide supporting signals
- Financial and behavioral features improve prediction confidence

## 8. Limitations

- Dataset size is small (500 rows)
- Engineered features are relatively simple
- Some features may be correlated (multicollinearity risk)

## 9. Future Improvements

To enhance feature engineering:

### Add behavioral features:
- Customer engagement metrics
- Usage frequency

### Use advanced techniques:
- Polynomial features
- Feature interactions using libraries like FeatureTools

### Additional improvements:
- Apply SHAP values for interpretability
- Perform feature selection to reduce redundancy

## 10. Conclusion

Feature engineering significantly improved model performance by introducing meaningful business-driven features.

### Key takeaways:

- Financial and behavioral features are strong churn indicators
- Tenure remains the most critical predictor
- Proper pipeline integration ensures scalability and reliability

The engineered feature set provides a strong foundation for building production-ready churn prediction systems.
