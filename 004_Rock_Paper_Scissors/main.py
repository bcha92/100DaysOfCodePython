# Rock Paper Scissors
import random # Importing Random module for CPU choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def render(choice: int, who: str):
    if choice == 0:
        selection = 'Rock'
        picture = rock
    elif choice == 1:
        selection = 'Paper'
        picture = paper
    else:
        selection = 'Scissors'
        picture = scissors
    
    print(f"\n{who} chose:", selection)
    print("\n", picture, "\n")

def who_wins(p1: int, p2: int):
    if p1 == p2:
        return "D" # Condition for Draw
    elif p1 > p2:
        if p1 == 2 and p2 == 0: return "P2"
        else: return "P1"
    else:
        if p2 == 2 and p1 == 0: return "P1"
        else: return "P2"

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