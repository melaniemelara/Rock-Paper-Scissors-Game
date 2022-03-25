# importing a package to extend python (just like we extended sublim, atom, or vscode)
from random import randint

# [] => this is an array
# variable(name) = [value1, value2, value3]
# an array is a special type of container that can hold multiple items
# arrays are indexed (their contents are assigned a number)
# the index always start at 0
# choices = [0 = "rock", 1 = "paper", 2 = "scissors"]
choices = ["rock", "paper", "scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3

# version 1, to explain array indexing
# player_choice = choices[1]
# player_choice = "paper"
# print("index 1 in the choice array is " + player_choice + ", which is paper")

player_choice = input("choose rock, paper, or scissors: ")

print("user chose: " + player_choice)

#this wll be the AI choice -> a random pick from the choices array
computer_choice = choices[randint(0, 2)]

print("computer chose: " + computer_choice)

if computer_choice == player_choice:
    print("tie")

elif computer_choice == "rock":
    if player_choice == "scissors":
        print("you lose!")
        # verbose way looks like this: player_lives = player_lives - 1
        # simplified way looks like this:
        player_lives -= 1
    else:
        print("you win!")
        computer_lives -= 1

elif computer_choice == "paper":
    if player_choice == "scissors":
        print("you win!")
        computer_lives -= 1
    else:
        print("you lose!")
        player_lives -= 1

elif computer_choice == "scissors":
    if player_choice == "paper":
        print("you lose!")
        player_lives -= 1
    else:
        print("you win!")
        computer_lives -= 1

print("Player Lives:", player_lives)
print("Computer Lives:", computer_lives)

