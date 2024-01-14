# Rock Paper Scissors
import random # Importing Random module for CPU choice
from functions import render, who_wins

p_score = 0
c_score = 0
game_run = True

while game_run == True:
    p_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: ")
    if p_choice == '': p_choice = 4 # defaults to Scissors
    else: p_choice = int(p_choice)
    
    c_choice = random.randint(0, 2)
    render(p_choice, 'You')
    render(c_choice, 'Computer')
    winner = who_wins(p_choice, c_choice)
    if winner == 'D': print("It's a Draw!")
    elif winner == 'P1':
        p_score += 1
        print("You Win!")
    else:
        c_score += 1
        print("You Lose!")
    print(f"\nThe current score is:\nPlayer: {p_score}\nComputer: {c_score}")
    
    exit_query = ''
    while exit_query.lower() != 'n' or exit_query.lower() != 'y':
        exit_query = input("\nWould you like to continue playing? Yes (Y) or No (N): ")
        if exit_query.lower() == "y" or exit_query.lower() == 'yes':
            print("You have decided to play another round!\n")
            break
        elif exit_query.lower() == "n" or exit_query.lower() == 'no':
            game_run = False
            break
        else:
            print("Invalid selection. Please try again!\n")

print("\nThank you for playing Rock, Paper, Scissors!\n")
exit() #Exits the game