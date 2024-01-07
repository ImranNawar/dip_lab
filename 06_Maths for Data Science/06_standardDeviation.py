# Standard Deviation
"""
Created on Sun Jan  7 10:57:26 2024

@author: Imran Nawar
"""
from math import sqrt

data = [0, 1, 5, 7, 9, 10, 14]

def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum((v - mean) ** 2 for v in values) / (len(values) - (1 if is_sample else 0))
    return _variance

def std_dev(values, is_sample: bool = False):
    return sqrt(variance(values, is_sample))

#print(std_dev(data))
print("VARIANCE = {}".format(variance(data, is_sample=True)))
print("STD DEV = {}".format(std_dev(data, is_sample=True)))