# Functions Module for Rock, Paper, Scissors
from art import rock, paper, scissors

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