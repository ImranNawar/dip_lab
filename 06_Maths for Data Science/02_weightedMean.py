# Weighted Mean
"""
Created on Sat Jan  6 18:48:24 2024

@author: Imran Nawar
"""
# Three exams of .20 weight each and final exam of .40 weight
sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40]
weighted_mean = sum(s * w for s,w in zip(sample, weights)) / sum(weights)
print(weighted_mean) 