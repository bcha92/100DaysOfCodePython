# Library Module for Number Guessing Game
logo = '''
   ___                  _   _            _ _   
  / __|_  _ ___ ______ | |_| |_  ___   _| | |_ 
 | (_ | || / -_|_-<_-< |  _| ' \/ -_) |_  .  _|
  \___|\_,_\___/__/__/  \__|_||_\___| |_     _|
                                        |_|_|  
'''

def welcome_message():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def is_difficult():
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if dif.lower() == "easy": return False
    elif dif.lower() == "hard": return True
    else:
        print("Invalid response, please type and enter 'easy' or 'hard'!")
        return is_difficult()

def guess_a_number():
    try:
        val = int(input("Make a guess: ")) 
        return val
    except ValueError:
        print("Invalid entry. Please enter an integer!")
    return guess_a_number()

def guess(chosen: int, chances: int):
    if chances == 0:
        print(f"\nSorry! You have no more attempts remaining.\nThe number I was thinking of was: {chosen}.")
    else:
        print(f"You have {chances} attempts remaining to guess the number.")
        n = guess_a_number()
        
        if n == chosen: print(f"\nCongratulations! You have correctly guessed the number I was thinking: {chosen}")
        elif n < 1 or n > 100:
            print("You are out of bounds. Please guess a number between 1 and 100!")
            chances -= 1
            guess(chosen, chances)
        elif n > chosen:
            print("Too high. Guess again.")
            chances -= 1
            guess(chosen, chances)
        else:
            print("Too low. Guess again.")
            chances -= 1
            guess(chosen, chances)