# Functions Module for PyPassword Generator
def exit_protocol():
    print("\nThank you for using the PyPassword Generator. Goodbye!\n")
    exit()

def invalid_message(message: str): return f"Invalid entry. Please enter {message}."

def yes_or_no(prompt: str, defaultValue: bool):
    ans = ''
    esc = ans.lower() != 'yes' or ans.lower() != 'y' or ans.lower() != 'no' or ans.lower() != 'n'
    while esc:
        ans = input(prompt + " (Y for Yes or N for No): ")
        if ans == '': return defaultValue
        elif ans.lower() == 'yes' or ans.lower() == "y": return True
        elif ans.lower() == 'no' or ans.lower() == 'n': return False
        else:
            print(invalid_message('Y for Yes or N for No'))
    return False # All Else Fail Value

def set_value(prompt: str, val: type, errorMessage: str, condition: bool):
    while condition:
        try: return val(input(prompt))
        except ValueError: print(errorMessage)
    return val(input(prompt)) # All Else Fail Value

def set_min_max_value(prompt: str, max: int, defaultValue: int, condition: bool):
    while condition:
        try:
            ans = input(prompt)
            if ans == '': return defaultValue
            elif int(ans) <= 0: return 0
            elif int(ans) <= max: return int(ans)
            else: print(f"Integer is out of bounds. Please enter a number between 0 and {max}.")
        except ValueError: print(f"Invalid entry. Please enter a number between 0 and {max}.")
    return 0 # All Else Fail Value