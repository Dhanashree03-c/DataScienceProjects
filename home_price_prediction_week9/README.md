# House Price Prediction using Machine Learning

## Overview

This project builds a machine learning pipeline to predict house prices based on property characteristics.

Features used:

- Area
- Bedrooms
- Bathrooms
- Age
- Location
- Property Type

The project demonstrates the full machine learning workflow including:

- data preprocessing
- exploratory analysis
- model training
- model evaluation
- model optimization

## Project Structure
```
house-price-prediction
│
├── data
├── notebooks
├── src
├── outputs
└── README.md
```

## Models Used

- Linear Regression
- Polynomial Regression
- Decision Tree
- Random Forest

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Results

Random Forest achieved the best performance with the highest R² score.

Key features affecting house price:

1. Area
2. Location
3. Property Type

## Installation

```bash
pip install -r requirements.txt
```

## Run Notebook

```bash
jupyter notebook notebooks/house_price_prediction.ipynb
```

## Future Work

- Hyperparameter optimization
- Larger dataset
- Deploy model using Flask or Streamlit