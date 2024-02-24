# Higher Lower Game
import random
from data import data
from art import logo, vs

def prompt(compare_a, compare_b):
    print(f"\nCompare A: {compare_a['name']}, {compare_a['description']}, {compare_a['country']}.")
    print(vs)
    print(f"Against B: {compare_b['name']}, {compare_b['description']}, {compare_b['country']}.")

def spoil(compare_a, compare_b):
    print(f"{compare_a['name']} has {compare_a['follower_count']} followers compared to {compare_b['name']}'s {compare_b['follower_count']} followers.")

def get_answer():
    answer = input("Who has more followers? Type 'A' or 'B' (case insensitive): ").lower()
    if answer.lower() == 'a' or answer.lower() == 'b': return answer
    else:
        print("Invalid response! Please enter 'A' or 'B'.")
        return get_answer()

def congrat():
    salut = ['Well Done!', 'You did it!', 'Correct!', 'Bravo!', 'Right answer!']
    return salut[random.randint(0, len(salut) - 1)]

print(logo)
score = 0
game_end = False
a = random.randint(0, len(data) - 1)
b = random.randint(0, len(data) - 1)

# Only triggered if indexes 'a' and 'b' are the same
while not game_end:
    while a == b: b = random.randint(0, len(data) - 1)
    if data[a]['follower_count'] > data[b]['follower_count']: answer = 'a'
    else: answer = 'b'

    prompt(data[a], data[b])
    guess = get_answer()
    
    if guess == answer:
        score += 1
        print(f"\n{congrat()} Your score is now {score}.")
        spoil(data[a], data[b])
        
        if answer == 'b': a = b
        b = random.randint(0, len(data) - 1)
    else:
        game_end = True
        print("\nI'm sorry! That answer was incorrect.")
        spoil(data[a], data[b])
        print(f"Your final score is: {score}. Thank you for playing Python Higher or Lower Game!")