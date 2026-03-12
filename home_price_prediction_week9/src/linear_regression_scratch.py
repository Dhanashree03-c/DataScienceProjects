"""
Linear Regression implemented from scratch using Gradient Descent.

This implementation is created for educational purposes to understand
how machine learning algorithms work internally without using
pre-built libraries like scikit-learn.
"""

import numpy as np

class LinearRegressionScratch:
    #Initialize model parameters.
    def __init__(self, learning_rate=0.00000001, epochs=1000):
        self.lr = learning_rate  #learning rate for gradient descent
        self.epochs = epochs     #total training iterations
        self.weights = None      #model coefficients
        self.bias = None         #model intercept

    #Train the linear regression model using gradient descent.
    def fit(self, X, y):
        """
        Train the model using gradient descent.
        """
        #number of samples (rows) and features (columns)
        n_samples, n_features = X.shape

        #initialize weights and bias to zero
        self.weights = np.zeros(n_features)
        self.bias = 0

        #gradient descent loop
        for _ in range(self.epochs):

            #predicted values using current weights
            y_pred = np.dot(X, self.weights) + self.bias

            #calculate gradients (partial derivatives)
            #derivative of loss function w.r.t weights
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            
            #derivative of loss function w.r.t bias
            db = (1 / n_samples) * np.sum(y_pred - y)

            #update weights and bias using gradient descent
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    #Generate predictions using the trained model.
    def predict(self, X):

        return np.dot(X, self.weights) + self.bias