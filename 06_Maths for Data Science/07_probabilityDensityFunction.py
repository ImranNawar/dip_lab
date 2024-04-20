# Probabality density function
"""
Created on Fri Apr 19 18:18:41 2024

@author: Imran Nawar
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gaussian_density(x, mu, sigma):
    return (1/np.sqrt(2*np.pi*np.power(sigma, 2))) * np.exp(-np.power(x - mu, 2) / (2 * np.power(sigma, 2)))


def plot_gaussian(x, mu, sigma):

    y = gaussian_density(x, mu, sigma)

    plt.plot(x, y)
    plt.title('Gaussian Probability Density Function')
    plt.xlabel('x variable')
    plt.ylabel('probability density function')
    plt.show()
    

# Calculating Area Under the Curve Solution
def gaussian_probability(mean, stdev, x_low, x_high):
    return norm(loc = mean, scale = stdev).cdf(x_high) - norm(loc = mean, scale = stdev).cdf(x_low)


x = np.linspace(-10, 100, 1000)  # Generate an array of x values
mu = 40
sigma = 10

plot_gaussian(x, mu, sigma)
gaussian_probability(40, 10, 30, 50)

