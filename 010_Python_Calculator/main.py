# Python Calculator
from lib import operations, set_value

def calculator():
    num1 = set_value("What is the first number? ", float)
    should_continue = True
    for symbol in operations: print(symbol)

    while should_continue:
        operation_symbol = set_value("Pick an operation: ", str, ["+", "-", "*", "/"])
        num2 = set_value("What is the second number? ", float)

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = set_value(f"Would you like to continue calculating? Type 'yes' or 'no' or 'y' or 'n': ", str, ["yes", "no", "y", "n"])
        
        if should_continue == 'no' or should_continue == 'n': should_continue = False
        else: num1 = answer

    new_calculation = set_value(f"Would you like start a new calculation (Selecting 'no' or 'n' will proceed exit this program)? Type 'yes' or 'no' or 'y' or 'n': ", str, ["yes", "no", "y", "n"])
    if new_calculation == 'yes' or new_calculation == 'y': calculator()

calculator()
print("Thank you for using the Python Calculator! Goodbye.\n")
exit()