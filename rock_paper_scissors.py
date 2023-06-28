# random is a module
import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    # this is one of the ways to check users input in one line
    if user_input not in options:
        # this will ask users again to type rock paper scissors
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    # this is from the array above
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # the 'and' check both left and right statements and only if both are true it will run the print() function
    if user_input == "rock" and computer_pick =="scissors":
        print("You won!")
        user_wins += 1
    
    elif user_input == "paper" and computer_pick =="rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick =="paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost")
        computer_wins += 1
    

print("Bye bye")