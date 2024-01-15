# Secret Auction
from lib import bid_finish_message, clear, set_value, exit_protocol

bids = {}
ongoing = True
winner_name = ''

print("Welcome to the secret auction program!\n")
while ongoing:
    name = set_value("What is your name? ", str)
    
    while name in bids: # Triggered if name already exist in auction pool
        print(f"Uh oh! It looks like there's another bidder with the name {name}.")
        changeName = set_value(f"If you are bidder registered as '{name}', would like to change your bid instead? Type 'yes' or 'no' or 'y' or 'n': ", str, ["yes", "no", "y", "n"])
        if changeName == 'yes' or changeName == 'y': break # Goes straight to change bid amount
        else:
            changeName = set_value("Would you like to change your name (Selecting 'no' or 'n' will proceed straight to announcing the winner (if any))? Type 'yes' or 'no' or 'y' or 'n': ", str, ["yes", "no", "y", "n"])
        
            if changeName == 'no' or changeName == 'n': # Goes straight to announcing winner
                ongoing = False
                break
            else: name = set_value("What will be your (new) name? ", str)
    if ongoing == False: break # Only triggered if going straight to announcing winner
    
    bids[name] = set_value("What is your bid? $", int)
    
    other = set_value("Are there any other bidders? Type 'yes' or 'no' or 'y' or 'n': ", str, ["yes", "no", "y", "n"])
    if other == 'no' or other == 'n': ongoing = False
    else: clear() # Clears screen to maintain secrecy!

for name in bids: # Calculates largest bids
    if winner_name == '' or bids[name] > bids[winner_name]: winner_name = name

# Big Announcement (or a flop)!
if len(bids) > 0: bid_finish_message(winner_name, bids[winner_name])
else: exit_protocol() # Chances are this will never happen, but just in case!