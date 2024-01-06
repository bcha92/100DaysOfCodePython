# Tip Calculator
def setValue(prompt, defaultVal, valType):
    val = input(prompt)
    if val == '':
        val = defaultVal
    if valType == int: val = int(val)
    elif valType == float: val = float(val)
    return val

def exitTransition():
    print("Thank you for using the Tip Calculator!")
    exit()

print("Welcome to the Tip Calculator!")
c = setValue("Please enter the currency symbol you want to use (default: \"$\"): ", "$", str)
amt_total = round(setValue(f"Please enter the total amount of your bill (default: {c}0.00): {c}", 0, float), 2)

if amt_total <= 0: #Goodbye message for an empty bill
    print("It seems like you don't have any outstanding bill to pay.")
    tip_custom = round(setValue(f"Please enter a custom tip amount (default: {c}0.00): {c}", 0, float), 2)
    print(f"The custom tip amount you have entered is {c}{tip_custom}")
    exitTransition()
    
else:
    num_people = setValue(f"How many people are splitting this bill (default: 1)? ", 1, int)
    tip_percent = setValue(f"How much tip are you planning to give in % (default: 0): ", 0, float)
    
    if tip_percent <= 0: tip_amount = setValue(f"Since you entered a value of 0% or less, please enter a custom tip amount (default: {c}0.00)? {c}", 0, float)
    else: tip_amount = round((amt_total / num_people) * (tip_percent / 100), 2)
    
    if num_people <= 1:
        print(f"Your tip amount will be {c}{tip_amount} based on")
        if tip_percent <= 0: print(f"the custom value you entered based on you portion value of {c}{amt_total}.")
        else: print(f"your tipping percentage of {tip_percent}% of your total bill of {c}{amt_total}.")
    
    else:
        print(f"For a party of {num_people} splitting the total bill of {c}{amt_total}, your tip amount will be {c}{tip_amount}.")
        if tip_percent <= 0: print(f"This is based on the custom value you entered based on your portion value of {c}{round(amt_total / num_people, 2)}.")
        else: print(f"This is based on {tip_percent}% tipping percentage of your approximate portion value of {c}{round(amt_total / num_people, 2)}.")
    exitTransition()
