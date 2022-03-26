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

# True or False are Bolean data types
# essentially, Boleans are equivalent to an on or off switch, 1 or 0, it is always totally true or totally false 
player_choice = False

# define a win or lose function
def winorlose(status):
    # version 1 of function
    # print("Inside winorlose function; status is: ", status)
    print("You", status, "Would you like to play again?")
    choice = input("Y / N? ")

    if choice == "N" or choice == "n":
        print("You chose to quit! Better luck next time!")
        exit()
    elif choice == "Y" or choice == "y":
        # reset the player lives and computer lives
        # and reset player choice to False, so our loops restarts
        global player_lives
        global computer_lives
        global total_lives

        player_lives = total_lives
        computer_lives = total_lives
    else:
        print("Make a valid choice - Y or N")
        # this might generate a bug that we need to fix later
        choice = input("Y / N? ")

# player_choice == False
# while player_choice (is==) False
while player_choice == False:
    print("====================*/ RPS GAME! */====================")
    print("Computer Lives:", computer_lives, "/", total_lives)
    print("Player Lives:", player_lives, "/", total_lives)
    print("=======================================================")
    # version 1, to explain array indexing
    # player_choice = choices[1]
    # player_choice = "paper"
    # print("index 1 in the choice array is " + player_choice + ", which is paper")

    player_choice = input("choose rock, paper, or scissors: \n")
    # player choice now equals TRUE because it has a value

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

    if player_lives == 0:
        winorlose("lose")

    if computer_lives == 0:
        winorlose("won")
       
    print("Player Lives:", player_lives)
    print("Computer Lives:", computer_lives)

    # map the loop keep running, by setting player_choice back to False
    # unset, so that our loop condition will evaluate to True
    player_choice = False

