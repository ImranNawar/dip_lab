# Linear Algebra
"""
Created on Sat Feb 10 10:51:42 2024

@author: Imran Nawar
"""
# Matrix multiplication
import numpy as np

A = [[2,3],[2,4]]
B = [[3,2],[5,3]]

C = np.dot(A, B) # np.matmul() can also be used
print("The Output matrix: C = ", C)


# Transpose of matrix
transpose_matrix1 = np.transpose(A)
print(transpose_matrix1)

transpose_matrix2 = np.array(A).T
print(transpose_matrix2)


# Calculating determinant
D = np.linalg.det(A)
print("Matrix =", A)
print("Determinant =", D)


# Calculating inverse of a matrix
inverse_A = np.linalg.inv(A)
print("inverse of matrix A: ", inverse_A)


# Solve a system of equations
# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72
A = [[4, 2, 4],
     [5, 3, 7],
     [9, 3, 6]]
B = [44,56,72]

X = np.linalg.inv(A).dot(B)
print(X) # [ 2. 34. -8.]