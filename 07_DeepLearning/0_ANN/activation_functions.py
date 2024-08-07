import numpy as np

# Tanh
def tanh(x):
    return (np.exp(x)) - np.exp(-x) / np.exp(x) + np.exp(-x)

# ReLU
def relu(x):
    return np.where(x > 0, x, 0)

# Linear
def linear(x):
    return x

# Softmax - Unlike other activations, softmax is performed on top of an array of values
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))
