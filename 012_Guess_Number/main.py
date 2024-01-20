# Number Guessing Game
import random
from lib import welcome_message, is_difficult, guess

welcome_message()
n_chosen = random.randint(1, 100)
is_hard = is_difficult()

if is_hard: attempts = 10
else: attempts = 20

guess(n_chosen, attempts)
print("Thank you for playing the Python Number Guessing Game!")