# Computer guessing number game
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback!='c':
        guess = random.randint(low, high)
        feedback = input(f"Is your number {guess}? (h)igher, (l)ower, (c)orrect: ")

        if feedback == 'h':
            print("Your guess is high")
            low = guess
            guess = random.randint(low, high)

        elif feedback == 'l':
            print("Your guess is low")
            high = guess
            guess = random.randint(low, high)

        elif feedback == 'c':
            print("yeah! Guess is right.")
            break

print(computer_guess(100))


