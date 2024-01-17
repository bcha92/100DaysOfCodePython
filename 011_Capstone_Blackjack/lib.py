# Library Module for Blackjack Game
import random

## Fixed Variables Library
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
card_values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
yn_escapes = ['yes', 'no', 'y', 'n'] # Yes or No escape values for set_values()

## Welcome/Exit Modules
def welcome_message():
    print(logo)
    print("\nWelcome to Python Blackjack!")

def exit_protocol():
    print(f"\nThank you for playing Python Blackjack. Goodbye!\n")
    exit()

## Generate and Input/Output Functions
def generate_deck():
    cards = []
    for suit in suits:
        for val in card_values: cards.append((val, suit))
    random.shuffle(cards)
    return cards

def generate_shoe(decks: int=1):
    shoe = []
    for _ in range(decks):
        shoe.extend(generate_deck())
    random.shuffle(shoe)
    print(f"A new shoe with {decks} decks has been added to the game.")
    return shoe

def refill_shoe(shoe: list, min_to_refill: int, decks: int):
    if len(shoe) < min_to_refill: shoe.extend(generate_shoe(decks))

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

def set_player_bet(total: float):
    player_bet = set_value(f"How much money do you want to bet (bank: ${total})? $", float)
    if player_bet < 1 or player_bet > total:
        print(f"Invalid Entry: Please enter a value 1 to {total}")
        return set_player_bet(total)
    
    if player_bet == total: print("Wow, you're going all in!")
    proceed = set_value(f"You have wagered ${player_bet}. Would you like to proceed with this bet (yes/no)? ", str, yn_escapes)
    if proceed == 'no' or proceed == 'n': return set_player_bet(total)
    else: return player_bet

def card_name(card: tuple):
    if type(card[0]) is int: return f"{card[0]} of {card[1]}"
    else: # Non-numerical face cards
        if card[0] == "J": name = "Jack"
        elif card[0] == "Q": name = "Queen"
        elif card[0] == "K": name = "King"
        else: name = "Ace"
        return f"{name} of {card[1]}"

def card_value(card: tuple):
    if type(card[0]) is int: return card[0]
    elif card[0] == "A": return 11
    else: return 10 # J, Q, K

def is_blackjack(hand: list):
    if len(hand) == 2 and card_value(hand[0]) + card_value(hand[1]) == 21: return True
    else: return False

def update_score(score: list, card: tuple):
    for i, s in enumerate(score):
        score[i] = (s + card_value(card))
        if len(score) > 1 and score[i] > 21: score.pop(i)


def is_bust(score: list):
    if len(score) == 1 and score[0] > 21: return True
    elif len(score) == 1 and score[0] <= 21: return False
    else:
        all_bust = True
        for s in score:
            if s <= 21: all_bust = False
        return all_bust

def best_score(hand: list):
    p_score = 0.0
    n_of_aces = 0
    for card in hand:
        p_score += card_value(card)
        if card_value(card) == 11: n_of_aces += 1
    if n_of_aces == 0: return int(p_score)
    
    scores = [p_score]
    for _ in range(n_of_aces):
        p_score -= 10
        scores.append(p_score)
    best_score = 0.0
    for s in scores:
        if s > best_score and s <= 21: best_score = s
    return int(best_score)

# Gameplay Functions
def card_list(hand: list, hidden: bool=False):
    for i, card in enumerate(hand):
        if i == 0 and hidden: print("Face Down Card")
        else: print(card_name(card))

def show_screen(p_hand: list, d_hand: list, p_score: list, d_score: list, bank: float, wager: float, insurance: float, i_hide: bool=False, hidden: bool=False):
    print("\nDealer's Cards:\n")
    card_list(d_hand, hidden)
    
    print("\nPlayer's Cards:\n")
    card_list(p_hand)
    
    print("\nDealer Score:", best_score(d_hand))
    print("Player Score:", best_score(p_hand))
    print(f"\nPlayer Bank: ${bank}")
    print(f"Current Bet: ${wager}")
    if i_hide: print("BlackJack Insurance: N/A\n")
    elif insurance > 0: print(f"BlackJack Insurance: ${insurance}\n")
    else: print("BlackJack Insurance: Opt-Out\n")

def deal_card(user: str, hand: list, score: list, shoe: list, hidden: bool=False):
    card = shoe.pop()
    hand.append(card)
    if card[0] == "A": score.append(score[-1] - 10)
    if not hidden: update_score(score, card)
    
    if hidden: print(f"A face down card has been drawn for the dealer.")
    else: print(f"{card_name(card)} has been drawn for the {user}.")


def init_deal(p_hand: list, d_hand: list, p_score: list, d_score: list, shoe: list):
    deal_card("player", p_hand, p_score, shoe)
    deal_card("dealer", d_hand, d_score, shoe, hidden=True) # Only the first dealer card is hidden
    deal_card("player", p_hand, p_score, shoe)
    deal_card("dealer", d_hand, d_score, shoe)

def d_blackjack_check(card: tuple, wager: float, bank: float):
    if card[0] == "A":
        print("POSSIBLE BLACKJACK WARNING! The dealer's second card is an ace!")
        print(f"Please note the blackjack insurance has a 2/1 payout.\nTherefore, the maximum insurance bet you can place is half of your original bet.\nIf the dealer has blackjack, you wil lose the wager, but you will receive the insurance payout instead.\nIf the dealer does not have blackjack, you will forfeit the insurance.")
        if bank == 0:
            print("Unfortunately, you don't have any money left in your bank to opt in for insurance.\nTherefore you are automatically opted out of blackjack insurance.")
            return 0
        else: 
            opt_in = set_value("Would you like to purchase insurance? ", str, yn_escapes)
            if opt_in == 'yes' or opt_in == 'y':
                proceed = False
                while not proceed:
                    insurance_bet = set_value(f"How much are you putting down for your blackjack insurance (between $0.01 and half of your bet: ${wager / 2})? $", float)
                    
                    while (insurance_bet < 0.01 or insurance_bet > wager / 2):
                        print(f"Invalid Entry: Please enter a value 1 to {wager / 2}")
                        insurance_bet = set_value(f"How much are you putting down for your blackjack insurance (between $0.01 and half of your bet: ${wager / 2})? $", float)
                    
                    proceed = set_value(f"You have wagered ${insurance_bet} for blackjack insurance. Would you like to proceed with this (yes/no)? ", str, yn_escapes)
                    if proceed == 'yes' or proceed == 'y':
                        proceed = True
                        bank -= insurance_bet
                print(f"You have purchased blackjack insurance for ${insurance_bet}. You now have ${bank} remaining in the bank.")
                return insurance_bet
            else:
                print("You have opted out of purchase blackjack insurance.")
                return 0
    else: return 0