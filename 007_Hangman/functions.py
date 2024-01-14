# Functions Module for Python Hangman
def letter_guess(used: list):
    guess = input("Guess a letter: ").lower()
    while guess.lower() not in list("abcdefghijklmnopqrstuvwxyz") or guess.lower() in used:
        print("Invalid Entry. Please select a single letter from A to Z! Or choose a letter you already have not used.")
        guess = input("Guess a letter: ").lower()
    return guess

def fill_slate(letter: str, word: str, slate: list):
    for i, l in enumerate(word):
        if l == letter: slate[i] = l
    print(f"You successfully guessed the letter '{letter}' in the word!")