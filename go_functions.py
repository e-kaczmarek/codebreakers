#
# TEXT-BASED ADVENTURE GAME
#
# CODEBREAKERS 2018
#

#
# go_functions.py
#
# allows user to move from room to room
#

import rooms


def go_north(room):
    #which room --> update current room
    if room = rooms.outside:
        print("You turn the handle of the door. The door is heavy, and creaks a lot as you push it, \
but you shove with all your might and it swings open. You appear to be in a hallway.")
        return rooms.main_hallway
    elif room = rooms.main_hallway:
        print("You go up the stairs. You are now on the upper landing.")
        return 
    print('You decide to go North.')
def go_south(room):
    print('You decide to go South.')
def go_east(room):
    print('You decide to go East.')
def go_west(room):
    print('You decide to go West.')

def go_into(room):
    if room = rooms.outside:
        print("You open the door to the house, and you're outside again. You breathe \
in deeply, allowing the fresh air to fill your lungs. It's a nice break from the musty\
 air that was inside. You see the sign in front of the house again.")
    elif room = rooms.basement:
        print("You slowly creep down the dark staircase. It is pitch black. You turn\
 on a lightswitch. A single lightbulb in the centre of the room flickers on dimly, lazily,\
 as if slightly annoyed that an intruder as imposed upon its long slumber. The room is\
  empty, save for a single mysterious box on the floor.")
    elif room = rooms.kitchen:
        print("You enter the kitchen. It's small and modest, with only a sink,\
 an oven, and a stove with a little tea kettle on top.")
    elif room = rooms.living_room:
        print("You enter the living room. It reminds you of a 1950s suburban house, \
with a couch, table, and a TV set. Oddly, you see no windows along the walls, although\
 you thought you had seen some outside.")
    elif room = rooms.main_hallway:
        print("The hallway is narrow. There is a kitchen to your left, a living room to \
your right, and a staircase that leads both up and down. Behind you is the front door, which\
 has not disappeared yet.")
    elif room = rooms.bedroom:
        print("You enter the bedroom. 
