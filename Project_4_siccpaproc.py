# Game scissor paper rock
import random

P1 = input("Player 1, please enter your choice 'r' for rock 's' for scissor and 'p' for paper : ")
computer = random.choice(['r', 's', 'p'])

if P1 == computer:
    print("Draw")

def win_game(P1, computer):
 if (P1 == 'r' and computer == 's') or (P1 == 's' and computer == 'p') or (P1 == 'p' and computer == 'r'):
        print("Player 1 win")

 elif (P1 == 'r' and computer == 'p') or (P1 == 's' and computer == 'r') or (P1 == 'p' and computer == 's'):
        print("Computer win")

print(win_game(P1, computer))