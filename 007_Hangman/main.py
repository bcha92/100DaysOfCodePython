# Python Hangman
from word_bank import words
from gallow import player_screen, dead_man
from functions import letter_guess, fill_slate

import random

chosen_word = random.choice(words) # Chooses a word from word bank by random
used_letters = [] # Tracker used to ensure you don't repeat a letter you've already used.
slate = [] # Slate used for UI visual for user
mistakes = 0 # Number of mistakes allotted before you lose the game.

for _ in range(len(chosen_word)):
    slate.extend("_")

# Game Logic
print("Welcome to Python Hangman. A word has been chosen from the word_bank.py file at random.")
print("Successfully solve the word to win! If you get 7 wrong guesses before you finish the word, the game is over!\n\nHere we go!")

while mistakes < 7:
    player_screen(slate, used_letters)
    guess = letter_guess(used_letters)
    
    if guess in list(chosen_word): fill_slate(guess, chosen_word, slate)
    else:
        dead_man(mistakes, guess)
        mistakes += 1
    used_letters.extend(guess)
    
    # End conditions!
    if mistakes == 7:
        print("Game Over! You Lose! The chosen word was: " + chosen_word)
    elif "_" not in slate:
        print(" ".join(slate))
        print("You win!")
        exit()