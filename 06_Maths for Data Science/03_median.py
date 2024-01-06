# Median
"""
Created on Sat Jan  6 18:50:24 2024

@author: Imran Nawar
"""
# The median is the middlemost values in the set of ordered values.

sample = [0, 1, 5, 7, 9, 10, 14]

def median(values):
    ordered = sorted(values)
    print(ordered)
    n = len(ordered)
    mid = int(n/2) - 1 if n % 2 == 0 else int(n/2)
    
    if n % 2 == 0:
        return (ordered[mid] + ordered[mid+1]) / 2.0
    else:
        return ordered[mid]
    
print(median(sample))