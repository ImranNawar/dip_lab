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
    
# While loop
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done!")

# For loop
for item in 'Python':
    print(item)
    
for item in range(10):
    print(item)
    
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

###
numbers = [5,2,5,2,2]
for x_count in numbers:
    total=''
    for count in range(x_count):
        total += 'x'
    print(total)
    
    
# To find the largest number in a list
numbers = [3,4,2,6,3,7,8,4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# list methods
list = [3,2,5,4,3,7]
print(list.index(5))
print(7 in list)
list.sort()
print(list)
list.reverse()
print(list)

# Write a program to remove duplicates in a list
numbers = [2,3,4,1,2,3,6,7]
new = []
numbers.sort()
for i in range(len(numbers)):
    if numbers[i] != numbers[i-1]:
        new.append(numbers[i])
print(new)

# Another approach
numbers = [2,3,4,1,2,3,6,7]
new = []

for number in numbers:
    if number not in new:
        new.append(number)
print(new)        

# Tuples are immutable, we cannot change it

# Unpacking  --- destructuring in javascript
coordinates = (3,2,4)
x,y,z = coordinates
print(x,y,z)

# Dictionaries
student = {
    'name': 'Imran',
    'age': 22,
    'is_programmaer': True
}
print(student['name'])

# Program to convert user input digits to numbers
dict = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
}

phone = input('Phone: ')
output = ""

for ch in phone:
    output += dict.get(ch) + ' '
    
print(output)

# Functions: Functions is a container for a few line of code to perform a specific task
# Parameters are placeholders defined in a function for recieving information.
# Arguments are actual pieces of information that are supplied to the function.

def greet_user():
    print("Welcome! ")
    print("This is a beautiful day")

print("start")
greet_user()
print('finish')

# Return statement
def square(number):
    return number * number
print(square(3))

# None is an object that represent the absence of a value

# Exceptions
try:
    age = int(input('Enter the age:  '))
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print("invalid value")
    
# Comments
# Use comments to explain why and how not what

# Use classes to define new types to define model real concepts
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print('Move')
    
    def draw(self):
        print('Draw')

# Object are the instance of the class, class is blueprint, each object is a different instance of class
point1 = Point(10, 20)
# point1.x = 10 # attributes
print(point1.x)
point1.draw()

# A constructot is a function that gets called at the time of creating an object
# Self references to the current object, self should be the first parameter of every method

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')
        
person1 = Person("Imran")
print(person1.name)
person1.talk()

# Inheritance
class Animal:
    def walk(self):
        print("walk")

class Dog(Animal):
    def bark(self):
        print('Dog bark')

class Cat(Animal):
    pass

dog1 = Dog()
dog1.walk()

# Packages
# Generating random values
import random

for i in range(3):
    print(random.random())
    
for i in range(3):
    print(random.randint(10,20))
    
member = ["Imran", "Wajahat", "Kaleem", "Fawad"]
leader = random.choice(member)
print(leader)

# Dice 
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        
        return first, second
    
dice = Dice()
print(dice.roll())


from pathlib import Path

path = Path()
for file in path.glob('*'):
    print(file)