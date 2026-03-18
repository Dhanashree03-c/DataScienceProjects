# Customer Churn Prediction Pipeline

## Project Overview

This project focuses on building a **robust data preprocessing and feature engineering pipeline** to predict customer churn in a telecom dataset.

Customer churn prediction helps businesses:
- Identify customers at risk of leaving
- Improve retention strategies
- Increase customer lifetime value

The project emphasizes **clean architecture, reusable code, and production-ready pipelines**.

## Objectives

- Perform data preprocessing and cleaning
- Apply multiple encoding techniques
- Implement feature scaling methods
- Engineer meaningful business features
- Detect and analyze outliers
- Build a reusable machine learning pipeline
- Evaluate model performance with proper metrics

## Project Structure
customer_churn_prediction_week10/
│
├── data/
│   └── churn_data.csv
│
├── notebooks/
│   └── churn_prediction_pipeline.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── outlier_handler.py
│   └── pipeline_builder.py
│
├── reports/
│   ├── preprocessing_report.md
│   └── feature_engineering_documentation.md
│
├── screenshots/
│   ├── dataset_preview.png
│   ├── churn_distribution.png
│   └── pipeline_output.png
│
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone Repository
git clone https://github.com/Dhanashree03-c/DataScienceProjects

cd customer_churn_prediction_week10

### 2. Create Virtual Environment

python -m venv venv

### 3. Activate Environment

**Windows:** venv\Scripts\activate

**Mac/Linux:** source venv/bin/activate

### 4. Install Dependencies

pip install -r requirements.txt

### 5. Run Notebook

jupyter notebook notebooks/churn_prediction_pipeline.ipynb

## Key Features

### Data Preprocessing
- Handling categorical variables
- Missing value validation
- Data consistency checks

### Encoding Techniques
- Label Encoding
- One-Hot Encoding
- Binary Encoding

### Feature Scaling
- StandardScaler
- MinMaxScaler

### Outlier Detection
- IQR Method
- Z-score Method

### Feature Engineering

Engineered features include:
- Customer Lifetime Value
- Average Revenue per Month
- Payment Efficiency
- Senior Citizen × Contract interaction
- Charge Difference

### Machine Learning Pipeline

Pipeline includes: FeatureEngineering → Encoding → Scaling → Model

- Built using `Pipeline` and `ColumnTransformer`
- Ensures reproducibility and consistency
- Prevents data leakage during inference

## Model Performance

| Metric         | Value   |
|----------------|---------|
| Accuracy       | ~96–97% |
| ROC-AUC        | ~0.99   |
| Recall (Churn) | 1.00    |

### Key Observations:
- Model captures **all churn customers (high recall)**
- Slight false positives (acceptable in business context)
- Strong generalization with cross-validation

## Business Insights

- Customers with **low tenure are highly likely to churn**
- **Higher monthly charges increase churn probability**
- **Month-to-month contracts** have the highest churn rate
- Long-term customers are more stable and valuable

## Evaluation Techniques

- Train-test split with stratification
- Cross-validation (StratifiedKFold)
- ROC-AUC scoring
- Confusion matrix analysis
- Classification report

## Limitations

- Small dataset (500 rows)
- Potential feature dominance (Tenure)
- Limited categorical diversity

## Future Improvements

- Apply SMOTE for class imbalance
- Use advanced models (XGBoost, LightGBM)
- Add SHAP for explainability
- Deploy using Flask or FastAPI
- Use larger real-world datasets

## Model Saving

Model is saved using `joblib`: model_bundle.pkl

Includes:
- Trained pipeline
- Feature schema

## Visual Outputs

The project generates:

- Churn distribution plot
- Monthly charges vs churn boxplot
- Confusion matrix
- ROC curve
- Feature importance chart

Stored in: screenshots/

## Key Strengths

- Clean and modular code structure
- Production-ready pipeline
- Strong feature engineering
- High model performance
- Business-aligned insights
- Reproducible workflow

## Author

**Dhanashree Tankar**

## Acknowledgements

Dataset inspired by telecom churn prediction problems.

## Note

This project demonstrates **end-to-end data preprocessing and feature engineering** with a strong focus on both **technical excellence and business understanding**, making it suitable for **internship and entry-level ML roles**.