# Python
"""
Created on Mon Mar  4 09:24:49 2024

@author: Imran Nawar
"""

# Python execute code line by line from top

print('Imran Nawar')

# Variable : to temporary store data in computer memory
name = 'John'
age = 20
new_player = True

# Recieving input
name = input('What is your name? ')
color = input('What is your faurite color? ')
print(name + ' likes ' + color)

# Type conversion
birth_year = input('What is your birth year? ')
age = 2024 - int(birth_year)
print(age)

# Ask the user their weight (pounds), convert it to kilograms
weight_lbs = input("Enter your weight in pounds: ")
weight_kg = int(weight_lbs) * 0.453592
print(weight_kg)

# Strings
course = 'Python for Beginners'
copy = course[:]
print(copy)
print(course[0:3])

# Formatted strings
first = 'Imran'
last = 'Nawar'
print(first + ' [' + last +'] is a coder')
print(f'{first} [{last}] is a coder')

# String methods
course = 'Python for Beginner'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('Py', 'XZ'))
print('Python' in course)

# Arithmetic Operation
x = (2 + 3) * 10 - 3
print(x)

# Math Functions
x = 2.9
print(round(x))
y = -2.5
print(abs(y))

import math
print(math.floor(y))

# if condition
is_hot = False
is_cold = True

if is_hot:
    print("It's hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's cold day")
    print("Wear warm clothes")
else:
    print("It's lovely day")
print('Enjoy your day')

# Logical operators
has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print('Eligible for loans')
    
if has_high_income or has_good_credit:
    print('Eligible for loans')
    
if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
    
# Comparison Operator
name = 'Imran'

if len(name) < 3:
    print('Name must be atleast three characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good')