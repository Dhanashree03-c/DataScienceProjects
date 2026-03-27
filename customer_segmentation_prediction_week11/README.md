# Customer Segmentation & Churn Prediction using Machine Learning

## Project Overview

Customer churn is a critical problem for subscription-based businesses. Retaining existing customers is often significantly more cost-effective than acquiring new ones. However, applying the same retention strategy to all customers is inefficient because different customers exhibit different behaviors and risk profiles.

This project uses **unsupervised learning to identify customer segments** and then trains **segment-specific machine learning models** to predict customer churn.

By combining **customer segmentation with predictive modeling**, the system enables businesses to design **targeted retention strategies for different customer groups**.

## Business Problem

Organizations often lose revenue due to customer churn without fully understanding the characteristics of customers who are most likely to leave.

Key challenges include:

* Identifying different **types of customers**
* Understanding **behavior patterns across segments**
* Predicting **which customers are likely to churn**
* Designing **segment-specific retention strategies**

This project addresses these challenges by integrating **clustering techniques and predictive modeling**.

## Project Objectives

The main objectives of this project are:

1. Preprocess customer data and prepare it for machine learning.
2. Segment customers into meaningful groups using clustering algorithms.
3. Analyze the characteristics of each customer segment.
4. Train separate churn prediction models for each segment.
5. Evaluate model performance using multiple metrics.
6. Extract business insights and provide recommendations.

## Machine Learning Pipeline

The project follows a structured ML workflow:

```
Raw Data
   ↓
Data Preprocessing
   ↓
Processed Dataset
   ↓
Customer Segmentation (Clustering)
   ↓
Segment Analysis
   ↓
Segment-Specific Prediction Models
   ↓
Model Evaluation
   ↓
Business Insights
```

## Technologies Used

* **Python**
* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **Scikit-Learn** – machine learning algorithms
* **Matplotlib & Seaborn** – data visualization
* **Joblib** – model serialization
* **Jupyter Notebook** – experimentation and documentation

## Algorithms Implemented

### Clustering Algorithms

* K-Means Clustering
* Hierarchical (Agglomerative) Clustering
* DBSCAN

### Prediction Model

* Random Forest Classifier

### Dimensionality Reduction

* Principal Component Analysis (PCA)

### Hyperparameter Optimization

* GridSearchCV

## Dataset

The dataset contains customer information such as:

| Feature          | Description                               |
| ---------------- | ----------------------------------------- |
| Tenure           | Number of months the customer has stayed  |
| MonthlyCharges   | Monthly service charges                   |
| TotalCharges     | Total charges accumulated                 |
| Contract         | Contract type                             |
| PaymentMethod    | Payment method used                       |
| PaperlessBilling | Whether billing is paperless              |
| SeniorCitizen    | Whether the customer is a senior citizen  |
| Churn            | Target variable indicating customer churn |

Dataset size:

* **500 rows**
* **Multiple categorical and numerical features**

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/Dhanashree03-c/DataScienceProjects.git
cd customer_segmentation_prediction_week11
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the Notebook

Launch Jupyter Notebook and run:

```
notebooks/customer_segmentation.ipynb
```

## Data Preprocessing

The preprocessing pipeline performs the following tasks:

* Removal of non-informative identifiers (`CustomerID`)
* Encoding categorical variables using `LabelEncoder`
* Creation of a clean dataset for modeling
* Saving the processed dataset for reproducibility

Processed dataset location:

```
data/processed/segmentation_data.csv
```

## Customer Segmentation

Three clustering algorithms were applied:

1. **K-Means Clustering**
2. **Hierarchical Clustering**
3. **DBSCAN**

The **Elbow Method** was used to determine the optimal number of clusters.

Results indicated that **three clusters provide meaningful segmentation**.

K-Means was selected as the primary segmentation method due to:

* Stable cluster assignments
* Clear separation of customer groups
* Interpretability for business analysis

## Customer Segments

Three major segments were identified:

| Segment   | Description                       |
| --------- | --------------------------------- |
| Segment 0 | Long-tenure high-value customers  |
| Segment 1 | Moderate tenure moderate spending |
| Segment 2 | High monthly charge customers     |

Each segment exhibits different spending behavior and churn risk.

## Segment-Specific Prediction Models

Instead of building a single model for all customers, **separate Random Forest models** were trained for each segment.

Advantages of this approach:

* Captures **different churn drivers across segments**
* Improves prediction accuracy
* Enables **segment-specific business strategies**

## Model Evaluation Metrics

The models were evaluated using multiple metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Example performance:

| Segment   | Accuracy | F1 Score |
| --------- | -------- | -------- |
| Segment 0 | 0.97     | 0.86     |
| Segment 1 | 1.00     | 1.00     |
| Segment 2 | 1.00     | 1.00     |

Due to the relatively small dataset, these scores may be optimistic and should be validated with larger datasets.

## Feature Importance Insights

Feature importance analysis revealed the most influential churn predictors:

1. **Tenure**
2. **Total Charges**
3. **Monthly Charges**
4. Contract type

Customers with shorter tenure and high charges showed higher churn risk.

## Business Insights

The segmentation results enable targeted retention strategies.

### Segment 0 – Loyal Customers

* Long tenure
* High lifetime value
* Low churn risk

Strategy:

* Loyalty rewards
* Premium support
* Exclusive upgrades

### Segment 1 – Moderate Customers

* Medium tenure
* Moderate spending

Strategy:

* Personalized offers
* Service bundles
* Flexible payment options

### Segment 2 – High Monthly Charge Customers

* High recurring charges
* Higher churn probability

Strategy:

* Pricing incentives
* Contract upgrades
* Retention campaigns

## Visualizations

The project includes several visualizations:

* Elbow method for cluster selection
* Customer cluster distribution
* PCA-based cluster visualization
* Feature importance plots

These visualizations help interpret the model results and communicate insights effectively.

## Limitations

* The dataset is relatively small (500 samples).
* Results may not generalize to larger real-world datasets.
* Further improvements could include additional behavioral features and external data sources.

## Future Improvements

Potential extensions of the project include:

* Using advanced clustering methods such as **Gaussian Mixture Models**
* Applying **XGBoost or Gradient Boosting models**
* Implementing **model explainability techniques (SHAP values)**
* Deploying the model as an **interactive dashboard using Streamlit**

## Author

**Dhanashree Tankar**

This project was developed as part of a **Data Science internship assignment focused on advanced machine learning techniques, customer segmentation, and churn prediction.**
