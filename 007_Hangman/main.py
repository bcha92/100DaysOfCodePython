# Hangman

## Example wordbank: Feel free to edit and use your own words as needed
word_bank = ["apple", "banana", "capitalism", "dairy", "elephant", "fantasy", "glory", "haunted", "igloo", "jalapeno", "kilogram", "lolipop", "morning", "nepotism", "oligarchy", "production", "quark", "rodeo", "sulfur", "talisman", "umbrella", "venison", "wonderful", "xylophone", "yokel", "zebra"]

## UI Strings
display_ui = [
    "\n---- ",
    "\n|  | ",
    "\n|    ",
    "\n|    ",
    "\n|    ",
    "\n|    ",
    "\n/---\\",
]

parts = [
    "\n|  O ",
    "\n|  | ",
    "\n| /| ",
    "\n| /|\\",
    "\n| /   ",
    "\n| / \\",
    "\n!! Final Warning !! You can only afford one more mistake or it's game over!"
]

import random

chosen_word = random.choice(word_bank) # Chooses a word from word bank by random
used_letters = [] # Tracker used to ensure you don't repeat a letter you've already used.
slate = [] # Slate used for UI visual for user
mistakes = 0 # Number of mistakes allotted before you lose the game.

for _ in range(len(chosen_word)):
    slate.extend("_")

def letter_guess():
    guess = input("Guess a letter: ").lower()
    while guess.lower() not in list("abcdefghijklmnopqrstuvwxyz") or guess.lower() in used_letters:
        print("Invalid Entry. Please select a single letter from A to Z! Or choose a letter you already have not used.")
        guess = input("Guess a letter: ").lower()
    return guess

def player_screen():
    print("".join(display_ui))
    print("")
    print(" ".join(slate))
    print("\nUsed Letters:", " ".join(used_letters))

def fill_slate(letter: str):
    for i, l in enumerate(chosen_word):
        if l == letter: slate[i] = l
    print(f"You successfully guessed the letter '{letter}' in the word!")

def dead_man(i: int, l: str):
    if i < 1: display_ui[2] = parts[i]
    elif i < 4: display_ui[3] = parts[i]
    else:
        display_ui[4] = parts[i]
    print(f"Wrong guess! The letter '{l}' was not found in the word!")
    if i == 5: display_ui.extend(parts[i + 1])

# Game Logic
print("Welcome to Python Hangman. A word has been chosen from the word_bank at random.")
print("Successfully solve the word to win! If you get 7 wrong guesses before you finish the word, the game is over!\n\nHere we go!")

while mistakes < 7:
    player_screen()
    guess = letter_guess()
    
    if guess in list(chosen_word): fill_slate(guess)
    else:
        dead_man(mistakes, guess)
        mistakes += 1
    used_letters.extend(guess)
    
    # End conditions!
    if mistakes == 7:
        print("Game Over! You Lose! The chosen word was: " + chosen_word)
    elif "_" not in slate:
        print("You win!")
        exit()