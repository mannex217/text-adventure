import time
print("To start, type \'start\'")
while True:
    fromUser = input()
    if fromUser == "start":
        print("Very well")
        break
    elif fromUser == "quit":
        print("good choice")
        break
    else:
        print("To start, type \'start\'")
fromUser = input()
# Variables
START_X = 0
START_Y = 0
MAP_X = 4
MAP_Y = 8

x = START_X
y = START_Y

# Commands
def go(direction):
    global x 
    global y 
    if direction == 'north':
        if (y + 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y += 1
            print()
    if direction == 'south':
        if (y - 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y -= 1
            print()
    if direction == 'east':
        if (x + 1) >= MAP_X:
            print("There's a wall there")
        else:
            x += 1
            print()
    if direction == 'west':
        if (x - 1) >= MAP_X:
            print("There's a wall there")
        else:
            x -= 1
            print()
