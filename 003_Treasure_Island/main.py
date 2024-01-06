print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Input prompt basic function
def setInput(prompt, exitWords):
    val = ''
    while val == '' or val not in exitWords:
        val = input(prompt)
        if val in exitWords: break
        print("Invalid entry! Please type one of these valid words to continue:", ", ".join(exitWords))
    return val

# First choice, left or right
print("You find a crossroad in the path ahead of you.")
path1 = setInput("Which way do you choose to go? Type 'left' or 'right': ", ['left', 'right'])

if path1 == 'right':
    print("\n Oops! Looks like a rockslide has blocked this path and you are unable to continue. Turning back and heading to the other direction of the crossroads.\n")
else: print("\nYou continue on your journey...\n")

print("You see a lake up ahead in front of you with an island in the middle. What is your next move?")
path2 = setInput("Will you 'swim' or 'wait' for a boat? ", ['swim', 'wait'])

if path2 == 'swim':
    print("\nIt turns out the lake you decided to swim in is a poisonous bog and has decided to pull you under it.\nOh dear, I'm afraid you have drowned and perished!\n\n☠️Game Over☠️\n")
    exit()
else:
    print("Waiting was a smart strategy as you began to notice the lake was not as swimmable as it seems.\nSoon enough, you see a boatman coming your way with a dinghy and you hop on for the ride to the other side!\n")

print("After you thank the boatman and go on your separate ways, you encounter a dilapadated house on the island and decide to enter.")
path3 = setInput("There are three doors in front of you: 'red', 'blue', and 'yellow'. Which one will you choose: ", ['red', 'blue', 'yellow'])

if path3 == 'red':
    print("After entering the red door, the door quickly locks itself behind you and you are trapped!\nYou see a carnivorous beast in the room and it attacks you as you scream for your life!\nAfter hearing the sounds of the bones crushing and your soul slowly leaving your body, you realize you were no more.\n\n ☠️Game Over☠️\n")
elif path3 == 'yellow':
    print("After entering the yellow door, you realize you entered a trap.\nA deep pit with a slowly sinking quicksand, you start feeling the despair as life is slowly drained from you as the quicksand pulls you under. You now just wait while you make peace with yourself.\n\n ☠️Game Over☠️\n")
elif path3 == 'blue':
    print("There is a chest in front of you as soon as you enter the room.\nYou check for traps, and once you open the chest, glimmers of diamonds and gold start pouring out from the coffers.\n\n 🎉 Congratulations! 🎉 👑 You found the lost treasure! 💎")
exit()