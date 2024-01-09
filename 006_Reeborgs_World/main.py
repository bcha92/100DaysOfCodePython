# Reeborg's World
# Note, this code will only work on Reeborg World's Website in the Maze puzzle:
# https://reeborg.ca/reeborg.html?name=Maze

import random

def turn_around():
    for _ in range(2): turn_left()

def turn_right():
    for _ in range(3): turn_left()

def left_is_clear():
    turn_left()
    clear = False
    if front_is_clear(): clear = True
    turn_right()
    return clear

def dead_end(): return wall_in_front() and wall_on_right() and not left_is_clear()

left_turns = 0
right_turns = 0

def random_direction(direction: str):
    if direction == "left":
        turn_left()
    elif direction == "right":
        turn_right()

while not at_goal():
    if front_is_clear():
        if left_is_clear() and right_is_clear():
            rand = ["left", "right", ""][random.randint(0,2)]
            random_direction(rand)
        elif left_is_clear():
            rand = ["left", ""][random.randint(0,1)]
            random_direction(rand)
        elif right_is_clear():
            rand = ["right", ""][random.randint(0,1)]
            random_direction(rand)
    elif wall_in_front():
        if left_is_clear() and right_is_clear():
            rand = ["left", "right"][random.randint(0,1)]
            random_direction(rand)
        elif right_is_clear():
            turn_right()
        elif left_is_clear():
            turn_left()
        else: turn_around()
    move()