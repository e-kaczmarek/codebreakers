#
# TEXT-BASED ADVENTURE GAME
#
# CODEBREAKERS 2018
#


#
# gameplay.py
#
# general purpose gameplay file
#



## IMPORT SLEEP?? ###
import rooms
from player_class import Player
import go_functions


def go(direction):
    # go a certain direction
    # valid directions are N/S/W/E
    ## add Forward, backward, outside, inside, left/right ######
    # check that you can go that way
    ## add check that the door isnt locked #####
    ## print at the end "You arrive in the ____. You see [list of items within the room]
    ## check if there are stairs where you want to move, #### particularly at the end of the
    ## hallways, attic, or basement
    ## OPTION: change rooms to a tree of nodes? ####
    if not player.current_room.can_go[direction]:
        print("Sorry, you can't go that way.")
    else:
        if direction == 'north':
            new_room = go_functions.go_north(player.current_room)
        elif direction == 'south':
            new_room = go_functions.go_south(player.current_room)
        elif direction == 'east':
            new_room = go_functions.go_east(player.current_room)
        elif direction == 'west':
            new_room = go_functions.go_west(player.current_room)
        else:
            print("cannot go that direction")
        player.current_room = new_room
        
         

#def take(item):
    ## check that you can pick it up
    ## add item to your inventory and remove it from the room's
    ## "You picked up {} !".format(item.name)
    ## "You cannot take that."

def inspect(room, item):
    ## print the item description from the room it's in
    ## call needs to be in the form inspect(rooms.<room>, 'item')
    print('you are inspecting', item)
    index = 0
    while room.items[index].name != item:
        index += 1
    print(room.items[index].description)

def help_function():
    print("Hello!")
    print("In this nifty help menu, I'll give you some ideas of how to perform actions\
    in the game, and how to write them in a way I'll understand.")
    print('If you want to move around, try writing "go <direction>", like "go north", for example.')
    print('If you want to pick something up, try writing "take <name of item>".')
    print('If you want to take a closer look at something, try writing "inspect <name of item>"')
    print("""If you want to try opening something up, write "open <name of item>" and we'll crack\
     that thing open for you.""")
    print("""If you decide you don't want to play anymore, simply type "quit" and the game will\
    end. Hope I helped!""")

#def open(item):
    ## check to make sure you can open it
    ## open item and list its contents
           
"""def choice(user_choice):
    # choice is a string of user input from "What do you want to do?"
    # should be in the form "go ____", "take ___", "look at/inspect ____", "help",
    # or "quit"
    choice_split = choice.split(' ')
    command = choice_split[0] ## first word in the choice string
    details = choice_split[1] ## rest of the word ##MAKE SURE THIS WORKS FOR MULTIWORDS
    switch_choice = {
        "go": go(details), ### IMPLEMENT THESE FUNCTIONS ###
        "walk": go(details),
        "take": take(details),
        "inspect": inspect(details),
        "open": 
        "help": help_function(),
        "quit": quit_function() ## MIGHT BE REDUNDANT ###
        }
    print(switch_choice.get(command.lower, "Sorry, I didn't understand that. Try again, \
or type 'help' for more options.") ###FIX THIS###
    """
#TEMPORARY
def choice(user_choice):
    # moves to go method
    if ('go' in user_choice) or ('walk' in user_choice):
        choice_split = user_choice.split(' ')
        direction = choice_split[-1].lower()
        if direction not in ['north', 'south', 'east', 'west']:
            print("That's not a valid direction. Try again.")
            return
        go(direction)
    elif 'help' in user_choice:
        help_function()
    elif ('inspect' in user_choice) or ('look at' in user_choice):
        choice_split = user_choice.split(' ')
        chosen_item = choice_split[-1].lower()
        inspect(player.current_room, chosen_item)
    else:
        print("Sorry, I didn't quite understand that. Try again, or input 'help' for more options.")

    
# Playing the Game

def playAdventure():
    print("Welcome to Codebreakers 2018 Adventures!\n")
    name = input("What is your name? ")
    global player
    player = Player(name)
    print("\nWelcome, {}! Remember, if you ever get lost or confused during the game, all you \
have to do is input 'help' and I'll tell you your options. Got it? Good!\n\nLet's get \
started!".format(player.name))
    print('\n')
    print('You are standing outside of an old house. You see a old sign out front and \
the front door appears to be the only way inside.\n')
    while True:
          user_choice = input("\nWhat do you want to do? ")
          if user_choice.lower() == 'quit':
              print("Thanks for playing!")
              return 
          choice(user_choice)


playAdventure()
    
