# Coffee Machine
from data import MENU, resources


def set_value(prompt: str, val: type = str, exit_words: list = None):
    if exit_words is None:
        exit_words = []

    try:
        value = val(input(prompt))

        if len(exit_words) > 0:
            while value not in exit_words:
                print(f"Invalid exit word. Value must be one of the following: {exit_words}")
                value = val(input(prompt))

        if val == str:
            value = value.lower()

        return value
    except ValueError:
        print(f"Invalid input. Value must be type of {val}")
        return set_value(prompt, val, exit_words)


def select_drink():
    sel = set_value(
        "What would you like? (espresso/latte/cappuccino): ",
        exit_words=["espresso", "latte", "cappuccino", "report"]
    )

    if sel == "report":
        print("You have selected 'report'. Here are the current resources in stock:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${resources['till']}")
        return select_drink()

    print(f"You have chosen {sel}. This item costs ${MENU[sel]['cost']}")
    return sel


def check_resources(inventory, s):
    shortages = []

    for _, t in enumerate(s['ingredients']):
        if inventory[t] < s['ingredients'][t]:
            shortages.append(t)

    return shortages


def update_resources(inventory, s):
    for _, t in enumerate(s['ingredients']):
        inventory[t] -= s['ingredients'][t]
    return inventory


def selection(n: str):
    se = MENU[n]
    return se, check_resources(resources, se)


def inserted_money(cost: float, prev_inserted: float = 0.0):
    def coins_inserted(c_name: str, v: float, t: float):
        coins = set_value(f"How many {c_name}?: ", int)
        if coins > 0:
            print(f"You have inserted {coins} {c_name} valued at ${coins * v}")
            print(f"Your total inserted value is ${t + (coins * v)}")
        return t + (coins * v)

    print("Please insert coins.")
    t_inserted = 0.0 + prev_inserted

    while t_inserted <= cost:
        t_inserted = coins_inserted("quarters", 0.25, t_inserted)
        if t_inserted >= cost:
            break

        t_inserted = coins_inserted("dimes", 0.1, t_inserted)
        if t_inserted >= cost:
            break

        t_inserted = coins_inserted("nickles", 0.05, t_inserted)
        if t_inserted >= cost:
            break

        t_inserted = coins_inserted("pennies", 0.01, t_inserted)
        break

    # Enough Money
    if t_inserted >= cost:
        change = t_inserted - cost
        print(f"You have entered sufficient change for this purchase. Here is ${change} in change.")
        return t_inserted

    # Not enough money
    print(f"Sorry, that's not enough money. You are currently short by ${cost - t_inserted}")
    conti = set_value("Would you like to insert more money? (y/n): ", exit_words=['y', 'n'])
    if conti == 'y':
        return inserted_money(cost, t_inserted)
    else:
        print(f"Your purchase has been cancelled. Your inserted change of ${t_inserted} will be refunded to you.")
        return 0.0


exit_sel = False

while exit_sel is False:
    print("\nWelcome to the Coffee Machine!")
    s_name = select_drink()
    selected, short_inv = selection(s_name)

    while len(short_inv) > 0:
        print(f"Your selection for {s_name} cannot be processed for the following reasons:")
        for _, item in enumerate(short_inv):
            print(f"There is not enough quantity of {item}.")

        cont = set_value("Would you like to continue with another selection? (y/n): ", exit_words=['y', 'n'])

        if cont == 'n':
            exit_sel = True
            break
        else:
            print("\nPlease make another selection.")
            s_name = select_drink()
            selected, short_inv = selection(s_name)

    if exit_sel is True:
        break

    till_updated = resources['till'] + inserted_money(selected['cost'])
    resources = update_resources(resources, selected)
    resources['till'] = till_updated
    cont = set_value("Would you like to continue with another selection? (y/n): ", exit_words=['y', 'n'])

    if cont == 'n':
        break

# Exit Message
print("Thank you for using the Coffee Machine! Goodbye.")
exit()
