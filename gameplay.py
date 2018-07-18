#
# TEXT-BASED ADVENTURE GAME
#
# CODEBREAKERS 2018
#
#

### import player <<need??? ###

class Player: 
    
    name = ""
    current_room = "outside"
    inventory = []
    
    def __init__(self, name):
        self.name = name

   
class Item:
    name = ''
    can_take = False
    can_open = False
    description = "It is nondescript."
    def __init__(self, name, can_take, description):
        # where can_take is a Boolean value expressing the player's ability
        # to put the Item into their inventory and description is a string
        # description of the item, name is a string of the title of the object
        self.name = name
        self.can_take = can_take
        self.description = description
    def __repr__(self):
        return self.name


class Room:
    
    name = ''
    items = []
    can_go = {"North": False, "South": False, "East": False, "West": False}
    locked = False
    floor = 0

    def __init__(self, name, floor):
        # where name is a string and floor is an integer of 0, 1, 2, or 3
        # Note: you must initialize the can_go dictionary on its own to create
        #       a usable room.
        self.name = name
        self.floor = floor
     
    def add_item(self, item_name, can_take, item_description):
        # item_name and item_description must be strings, can_take is a boolean
        # adds an item of class Item to Room self
        new_item = Item(item_name, can_take, item_description)
        self.items += [new_item]
        
    def remove_item(self, item_name):
        # removes an item from the room
        # item_name must be a string
        if (item_name in self.items):
            self.items.remove(item_name)
        else:
            print("You cannot remove that item, sorry!")

    def get(self, item_name):
        # returns the item object
        for i in self.items:
            if i.name==item_name:
                return i
        print("Item could not be found.")

class House:
    ### ADD ITEMS, CAN_GO, AND LOCKED IF APPLICABLE ###
    
    outside = Room('outside', 1)
    # outside is a sign and the front door. the only direction you can move is inside the house
    outside.add_item('sign', False, "It is an old, wooden, worn-out sign. There are some faded \
words on it that you can only just make out. It reads: \n\nA TREASURE LIES BEHIND MY WALL. \nMY\
DARK ROOMS BECKON TO ALL WHO CALL. \nIN ORDER TO DRINK FROM THE GOLDEN CUP \n YOU MUST FIRST GO\
DOWN BEFORE GOING UP\n\nWhat could it mean?\n")
    outside.add_item('front door', False, "It is a wooden door. It appears to be unlocked.")
    outside.can_go["North"] = True

    
    basement = Room('basement', 0)
    # in the basement is a single object: the puzzle box. it is locked initally.
    # you can only move to the north, which is up the stairs
    basement.add_item('puzzle box', False, 'It is a strange box. Perhaps it contains something \
inside of it? If only you could figure out a way to open it...')
    basement.get('puzzle box').can_open = True
    basement.can_go["North"] = True
    basement.locked = True

    
    kitchen = Room('kitchen', 1)
    # in the kitchen is a sink, stove, oven, and tea kettle. You can only move
    # east, back into the main hallway
    kitchen.add_item('sink', False, "It is a rusty old sink. It doesn't appear to be working.")
    kitchen.add_item('stove', False, "It is an electric stovetop. It doesn't work. I guess you won't\
be cooking anything anytime soon.")
    kitchen.add_item('oven', False, "It is a nondescript oven, not in working condition. The \
electricity here must be out or something...")
    kitchen.get('oven').can_open = True
    kitchen.add_item('tea kettle', False, "It is a beautiful antique copper tea kettle.")
    kitchen.get('tea kettle').can_open = True
    kitchen.can_go["East"] = True

    
    living_room = Room('living room', 1)
    # in the living room is a couch, a table with drawers, and a TV set. You can only move
    # west, back into the main hallway
    living_room.add_item('couch', False, "It is a dusty couch. I wouldn't recommend sitting on it.")
    living_room.get('couch').can_open = True                         
    living_room.add_item('table', False, "It is a small wooden table with a drawer underneath.")
    living_room.get('table').can_open = True
    living_room.add_item('TV set', False, "It is a small television set from the 50s. You try to\
turn it on, but nothing happens. Bummer.")
    living_room.can_go["West"] = True

    
    main_hallway = Room('main landing hallway', 1)
    # no objects within this room. You can move in any direction.
    # North leads to the main landing stairway, South leads back outside, East leads to the
    # living room, and West leads to the kitchen
    main_hallway.can_go["North"] = True
    main_hallway.can_go["South"] = True
    main_hallway.can_go["East"] = True
    main_hallway.can_go["West"] = True

    
    bedroom = Room('bedroom', 2)
    # contains a bed, a nightstand table, and a closet. You can only move
    # east, back into the upper hallway
    bedroom.add_item('bed', False, "It is a twin-sized bed with floral sheets. It doesn't look\
very comfortable.")
    bedroom.add_item('nightstand table', False, "It is a small wooden nightstand table. It has\
a small drawer underneath.")
    bedroom.get('nightstand table').can_open = True
    bedroom.add_item('closet', False, "It looks like the door to a small walk-in closet. Do you\
think there's a portal to Narnia back there?")
    bedroom.get('closet').can_open = True
    bedroom.can_go["East"] = True

    
    bathroom = Room('bathroom', 2)
    # contains a toilet, sink, and mirror. You can only move west,
    # back into the upper hallway
    bathroom.add_item('toilet', False, "It is a generic porcelain toilet. Please don't try sticking your\
hand inside.")
    bathroom.get('toilet').can_open = True
    bathroom.add_item('sink', False, "It looks like a sink. What more can I say?")
    bathroom.add_item('mirror', False, "You see a confident young adventurer staring back at you.\
Oh wait, that's just you!")
    bathroom.get('mirror').can_open = True
    bathroom.can_go["West"] = True

    
    upper_hallway = Room('upper landing hallway', 2)
    # contains no objects. It is locked initially. Its key is located in the basement
    # puzzle box. You can move North to the upper stairway, West to the bedroom, or East
    # to the bathroom.
    upper_hallway.locked = True
    upper_hallway.can_go["North"] = True
    upper_hallway.can_go["West"] = True
    upper_hallway.can_go["East"] = True

    
    attic = Room('attic', 3)
    # contains a single object: Mystery. It is locked initially. Its key is located somewhere
    # on floor 2. You can only move North, back down the stairs.
    attic.locked = True
    attic.add_item('???', True, "It is a mysterious object")
    attic.can_go["North"] = True


#def go(direction):
    ## go a certain direction
    ## valid directions are N/S/W/E, Forward, backward, outside, inside, left/right
    ## check that you can go that way
    ## check that the door isnt locked
    ## print at the end "You arrive in the ____. You see [list of items within the room]
    ## check if there are stairs where you want to move, particularly at the end of the
    ## hallways, attic, or basement

#def take(item):
    ## check that you can pick it up
    ## add item to your inventory and remove it from the room's
    ## "You picked up {} !".format(item.name)
    ## "You cannot take that."

#def inspect(item):
    ## print the item description

#def help_function():
    ## print list of things you can do
    ## Hello! In this nifty help menu, I'll give you some ideas of how to perform actions
    ## in the game, and how to write them in a way I'll understand.
    ## If you want to move around, try writing "go <direction>", like "go north", for example.
    ## If you want to pick something up, try writing "take <name of item>".
    ## If you want to take a closer look at something, try writing "inspect <name of item>"
    ## If you want to try opening something up, write "open <name of item>" and we'll crack
    ## that thing open for you.
    ## If you decide you don't want to play anymore, simply type "quit" and the game will
    ## end. Hope I helped!

#def open(item):
    ## check to make sure you can open it
    ## open item and list its contents
           
"""def user_choice(choice):
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
def user_choice(choice):
    return
# Playing the Game

def playAdventure():
    print("Welcome to Codebreakers 2018 Adventures!\n")
    name = input("What is your name? ")
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
          user_choice(user_choice)
    
