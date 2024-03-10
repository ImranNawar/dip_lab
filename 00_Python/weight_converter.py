# Weight Converter Program
"""
Created on Mon Mar  4 19:18:27 2024

@author: PC
"""
weight = input('Weight: ')
unit = input("L(bs) of K(g): ")

if unit.upper() == 'K':
    weight = int(weight) / 0.453592
    print(f'You are {weight} pounds')
elif unit.upper() == 'L':
    weight = int(weight) * 0.453592
    print(f'You are {weight} kilograms')
else:
    print('Please enter K or L')


