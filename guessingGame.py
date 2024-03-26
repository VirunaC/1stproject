# Author - Viruna Cooray
# Date 26th March 2024
# Implement a guessing game using a while loop

import random

num = random.randint(1,10)
guess = None

while guess != num:
    guess = int(input("Enter your guess: "))
    
    if guess == num:
        print('Congratulations!!!, You guessed correct.')
    
    elif guess > num:
        print("Your number is too high")
     
    elif guess < num:
        print("Your number is too low")
