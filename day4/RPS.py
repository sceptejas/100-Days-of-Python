import random

CompChoice = random.randint(0, 2)
playerChoice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))

if playerChoice == 0:
    if CompChoice == 2:
        print("You win")
    elif CompChoice == 0:
        print("Draw")
    else:
        print("Computer wins")

elif playerChoice == 1:
    if CompChoice == 0:
        print("You win")
    elif CompChoice == 1:
        print("Draw")
    else:
        print("Computer wins")

elif playerChoice == 2:
    if CompChoice == 1:
        print("You win")
    elif CompChoice == 2:
        print("Draw")
    else:
        print("Computer wins")
