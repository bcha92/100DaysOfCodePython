# Password Generator
import random
from lib import lettersL, lettersU, numbers, symbols, use
from functions import exit_protocol, invalid_message, yes_or_no, set_value, set_min_max_value

letters = []

## PyPassword Generator Prompt Starts
final = True
while final:
    print("\nWelcome to the PyPassword Generator!\n")

    num_total = set_value("Enter the total number of characters for your password: ", int, invalid_message("an integer"), final)
    spare_total = num_total

    # Enable/Disable use of lowercase alphabet
    use["lower"] = yes_or_no("Do you want to use lowercase alphabet characters (a-z)? (Default: Yes)", use["lower"])
    if use["lower"]: letters.extend(lettersL)

    # Enable/Disable use of uppercase alphabet
    use["upper"] = yes_or_no("Do you want to use uppercase alphabet characters (A-Z)? (Default: Yes)", use["upper"])
    if use["upper"]: letters.extend(lettersU)

    # Enable/Disable use of numbers
    use["numbers"] = yes_or_no("Do you want to use numbers (0-9)? (Default: Yes)", use["numbers"])
    if use["numbers"]:
        min_numbers = set_min_max_value(f"Enter the minimum of numbers to use in your password (default: 1, max: {spare_total}): ", spare_total, 1, final)
        if min_numbers <= 0: use["numbers"] = False
        else:
            letters.extend(numbers)
            spare_total -= min_numbers

    # Enable/Disable use of non-alphanumeric symbols
    if spare_total > 0:
        use["symbols"] = yes_or_no("Do you want to use symbols (i.e. ! # ? < +)? (Default: No)", use["symbols"])
        if use["symbols"]:
            min_symbols = set_min_max_value(f"Enter the minimum of symbols to use in your password (default: 1, max: {spare_total}): ", spare_total, 1, final)
            if min_symbols == 0: use["symbols"] = False
            else: letters.extend(symbols)

    if use["lower"] == False and use["upper"] == False and use["numbers"] == False and use["symbols"] == False:
        print("It seems like you don't want to use any alphabets, numbers, or symbols. Would you like to start over?")
        final = yes_or_no("Please select Y for Yes or N for No?\nNOTE: No selection or selecting N for No will terminate this program: ", False)
        
        if final == False: exit_protocol()
    else: final = False


## Character Aggregation based on previous prompts
continue_generating = True
if use["numbers"]: min_numbers_save = min_numbers
if use["symbols"]: min_symbols_save = min_symbols

while continue_generating:
    print("\nUser Configuration Input:\n")
    print("Number of characters in Password:", num_total)
    print("Use Lowercase Alphabet:", use["lower"])
    print("Use Uppercase Alphabet:", use["upper"])
    print("Use Numbers", use["numbers"])
    print("Use Symbols", use["symbols"])
    if use["numbers"]: print("\nMinimum use of Numbers:", min_numbers)
    if use["symbols"]: print("Minimum use of Symbols:", min_symbols)

    print("\n\nGenerating Password...\n")
    generated_password = ""
    for i in range(0, num_total):
        if use["symbols"] and min_symbols > 0:
            generated_password += symbols[random.randint(0, len(symbols) - 1)]
            min_symbols -= 1
        elif use["numbers"] and min_numbers > 0:
            generated_password += numbers[random.randint(0, len(numbers) - 1)]
            min_numbers -= 1
        else:
            generated_password += letters[random.randint(0, len(letters) - 1)]

    generated_password = list(generated_password)
    random.shuffle(generated_password)
    generated_password = "".join(generated_password)
    print("Here is your new Generated PyPassword:", generated_password)
    
    continue_generating = yes_or_no("\nWould you like to generate another new PyPassword? (default: No)", False)
    if continue_generating == False: exit_protocol()
    else:
        if use["numbers"]: min_numbers = min_numbers_save
        if use["symbols"]: min_symbols = min_symbols_save