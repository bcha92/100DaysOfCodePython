# Blackjack Game
from lib import welcome_message, exit_protocol, generate_shoe, refill_shoe, set_value, set_player_bet, yn_escapes, init_deal, d_blackjack_check, show_screen, is_blackjack, update_score, is_bust, deal_card, card_list, card_name, best_score

game_stopped = False
welcome_message()

while not game_stopped:
    # Sets parameters of new game
    start = set_value("Would you like to start a new game? ", str, yn_escapes)
    if start == 'no' or start == 'n':
        game_stopped = True
        break
    
    num_of_decks = set_value("How many decks would you like in the shoe (1 equals 52 cards)? ", int)
    shoe = generate_shoe(num_of_decks)
    player_bank = 1000
    
    # Game starts
    def game(game_shoe: list, total: float):
        #Previous game carryover
        refill_shoe(game_shoe, 4, num_of_decks)
        
        # Initial Game States
        dealer_hand = []
        d_card_hidden = True # Hides dealer's first card initially
        dealer_score = [0]
        
        player_hand = []
        player_score = [0]
        insurance_bet = 0
        player_bet = set_player_bet(total) # Set player wager
        total -= player_bet
        
        init_deal(player_hand, dealer_hand, player_score, dealer_score, game_shoe)
        show_screen(player_hand, dealer_hand, player_score, dealer_score, total, player_bet, insurance_bet, True, d_card_hidden)
        if is_blackjack(player_hand):
            print("Cool! You have a natural blackjack!")
            print(f"If the dealer doesn't have a natural blackjack as well, expect a payout of ${player_bet * 1.5}!\nOtherwise, you only get your original bet back!")
        insurance_bet = d_blackjack_check(dealer_hand[1], player_bet, total)
        # Checks if dealer has ace as face-up card. Returns 0 if no dealer has no face-up ace or player chooses insurnace opt-out. Otherwise, it will return a float value above 0 for insurance amount.
        
        # Player Turn to Deal Card(s)
        if not is_blackjack(player_hand):
            player_turn = True
            while player_turn:
                p_deal = set_value("Would you like to get a card? ", str, yn_escapes)
                if p_deal == "yes" or p_deal == "y":
                    deal_card("player", player_hand, player_score, game_shoe)
                    print("\nPlayer's Cards:\n")
                    card_list(player_hand)
                    print("\nPlayer Score:", best_score(player_hand))
                    if is_bust(player_score):
                        player_turn = False
                        print("Oops! You have been busted!")
                else: player_turn = False
        
        if not is_bust(player_score):
            d_card_hidden = False # Once player is finished face down card is revealed
            update_score(dealer_score, dealer_hand[0]) # Update score after reveal
            print(f"Dealer reveals face down card as {card_name(dealer_hand[0])}")
            if is_blackjack(dealer_hand): print("Dealer has blackjack!")
            else:
                print("Dealer draw cards until it stands at 17.\n")
                while min(dealer_score) < 17:
                    deal_card("dealer", dealer_hand, dealer_score, game_shoe)
                    if is_bust(dealer_score):
                        print("Oops! Dealer has been busted!")
                        break
            
            print("\nDealer's Cards:\n")
            card_list(dealer_hand)
            print("\nDealer Score:", best_score(dealer_hand))
        
        # Bet Payouts (if any):
        if is_blackjack(player_hand) and is_blackjack(dealer_hand):
            total += player_bet + (insurance_bet * 2)
            print(f"Since both you and the dealer have natural blackjacks, you receive back your original bet of ${player_bet}")
            if insurance_bet > 0: print(f"including your insurance payout of ${insurance_bet * 2}")
        elif is_blackjack(player_hand) and not is_blackjack(dealer_hand):
            total += (player_bet * 1.5)
            print(f"Since the dealer doesn't have a natural blackjack, you receive a 3:2 payout of ${player_bet * 1.5}, ")
        elif is_blackjack(dealer_hand):
            total += (insurance_bet * 2)
            print(f"Dealer wins with natural blackjack!")
            if insurance_bet > 0: print(f"But you did opt-in for insurance of ${insurance_bet},\ntherefore you receive the blackjack insurance payout of ${insurance_bet * 2}")
        elif is_bust(dealer_score) or (best_score(player_hand) > best_score(dealer_hand)):
            total += (player_bet * 2)
            if is_bust(dealer_score): print("Oops! Dealer has busted!")
            print(f"Player wins! ${player_bet * 2} has been added to your bank!")
        elif best_score(player_hand) == best_score(dealer_hand):
            total += player_bet
            print(f"Draw! Original bet of ${player_bet} has been returned to your bank!")
        else: print("Dealer wins!")
        
        # End Game Outcomes
        if total < 1: # Goes straight to start new game option
            if total == 0: print("\nOh dear, there's no more money left in the bank.")
            else: print(f"\nOh dear, you have only ${total} left in the bank. It is no longer enough to wage a minimum bet.\nYour final score is therefore {total - 1000}!")
        else:
            print(f"\nYou have ${total} in your bank!")
            start = set_value("Would you like to keep playing (yes) or cash out (no)? ", str, yn_escapes)
            if start == 'no' or start == 'n': # Cash Out
                game_stopped = True # breaks
                print(f"You have chosen to cash out. Your balance is ${total}. Your final score is {total - 1000}!")
            else: game(game_shoe, total) # Starts new game with current balance
    
    game(shoe, player_bank)

exit_protocol()