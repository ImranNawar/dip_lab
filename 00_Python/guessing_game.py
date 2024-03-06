# Guessing Game
"""
Created on Tue Mar  5 16:00:43 2024

@author: Imran Nawar
"""
import random

secret_number = random.randint(0,9)
guess_count = 0
while guess_count < 3:
    guess = int(input("Guess: "))
    guess_count = guess_count+1
    if guess == secret_number:
        print('You Won')
        break   
else:
    print("Sorry you failed!")