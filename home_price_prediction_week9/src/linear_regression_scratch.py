"""
Linear Regression implemented from scratch using gradient descent.
Used for educational understanding of ML fundamentals.
"""

import numpy as np


class LinearRegressionScratch:
    def __init__(self, learning_rate=0.00000001, epochs=1000):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """
        Train the model using gradient descent.
        """

        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):

            y_pred = np.dot(X, self.weights) + self.bias

            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        """
        Generate predictions.
        """
        return np.dot(X, self.weights) + self.bias