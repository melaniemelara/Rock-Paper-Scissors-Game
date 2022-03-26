from random import randint

choices = ["rock", "paper", "scissors"]
total_lives = 3
player_lives = total_lives
computer_lives = total_lives
player_choice = False

computer_choice = choices[randint(0, 2)]