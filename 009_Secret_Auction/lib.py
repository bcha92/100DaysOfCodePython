import math, os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def bid_finish_message(name: str, amount: int):
  print(logo, f"\n\nSold! The winner of this secret auction is {name} with a bid of ${amount}!\n")

def clear(): os.system("cls")

def exit_protocol():
  print("Thank you for using the secret auction progrm! Goodbye!")
  exit()

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