# Variance
"""
Created on Sun Jan  7 10:50:43 2024

@author: Imran Nawar
"""
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values)/len(values)
    _variance = sum((v - mean)**2 for v in values)/len(values)
    return _variance

print(variance(data))