# Python program to guess the number 

import random

def guess(x):
    guessed_num = random.randint(1, x)
    guess = 0
    while guess != guessed_num:
        guess = int(input(f"Enter your guess between 1 and {x}: "))

        if guess > guessed_num:
            print("Your guess is high")
        elif guess < guessed_num:
            print("Your guess is low")
        else:
            print("Congrats! You guess is correct.")


print(guess(10))