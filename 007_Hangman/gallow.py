# Gallow Art Module for Python Hangman
## UI Strings
main = [
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

def player_screen(slate: list, used_letters: list):
    print("".join(main))
    print("")
    print(" ".join(slate))
    print("\nUsed Letters:", " ".join(used_letters))

def dead_man(i: int, l: str):
    if i < 1: main[2] = parts[i]
    elif i < 4: main[3] = parts[i]
    else:
        main[4] = parts[i]
    print(f"Wrong guess! The letter '{l}' was not found in the word!")
    if i == 5: main.extend(parts[i + 1])