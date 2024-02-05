# Cost function
"""
Created on Mon Feb  5 12:16:59 2024

@author: Imran Nawar
"""
import numpy as np

def compute_cost(X, y, theta):
    """
    Compute the cost function for linear regression.
    
    Arguments:
    X -- input features (numpy array of shape (m, 2))
    y -- output values (numpy array of shape (m, 1))
    theta -- parameters (numpy array of shape (2, 1))
    
    Returns:
    J -- cost function value
    """
    m = len(y)  # number of training examples
    
    # Compute predictions
    predictions = np.dot(X, theta)
    
    # Compute squared errors
    squared_errors = (predictions - y) ** 2
    
    # Compute cost function value
    J = 1 / (2 * m) * np.sum(squared_errors)
    
    return J

# Example usage
X = np.array([[1, 1], [1, 2], [1, 3]])  # input features with bias term
y = np.array([[1], [2], [3]])            # output values
theta = np.array([[0], [0]])              # initial parameters

cost = compute_cost(X, y, theta)
print("Cost:", cost)

