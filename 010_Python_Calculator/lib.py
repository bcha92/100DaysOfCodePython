logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a: float, b: float): return a + b
def subtract(a: float, b: float): return a - b
def multiply(a: float, b: float): return a * b
def divide(a: float, b: float): return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def set_value(prompt: str, val: type, exit_words: list=[]):
  ans = ''
  while ans not in exit_words:
    try:
      ans = val(input(prompt))
      if val == str and len(exit_words) == 0:
        anslen = "".join(" ".split(ans))
        if len(anslen) > 0: return ans
        else: print(f"Invalid entry. Answer must be type {val} and longer than 0 characters and not just spaces.")
      elif val == str and len(exit_words) > 0:
        if ans.lower() in exit_words: return ans.lower()
        else: print(f"Invalid entry! Please answer one of the following: {', '.join(exit_words)}.")
      else: return ans
    except ValueError: print(f"Invalid entry. Answer must be of type {val}.")