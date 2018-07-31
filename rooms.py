#
# TEXT-BASED ADVENTURE GAME
#
# CODEBREAKERS 2018
#


#
# rooms.py
#
# contains all the rooms in the game, the room
#


class Room:
    
    name = ''
    items = []
    can_go = {"north": False, "south": False, "east": False, "west": False}
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



outside = Room('outside', 1)
# outside is a sign and the front door. the only direction you can move is inside the house
outside.add_item('sign', False, "It is an old, wooden, worn-out sign. There are some faded \
words on it that you can only just make out. It reads: \n\nA TREASURE LIES BEHIND MY WALL. \nMY\
DARK ROOMS BECKON TO ALL WHO CALL. \nIN ORDER TO DRINK FROM THE GOLDEN CUP \n YOU MUST FIRST GO\
DOWN BEFORE GOING UP\n\nWhat could it mean?\n")
outside.add_item('front door', False, "It is a wooden door. It appears to be unlocked.")
outside.can_go["north"] = True

    
basement = Room('basement', 0)
# in the basement is a single object: the puzzle box. it is locked initally.
# you can only move to the north, which is up the stairs
basement.add_item('puzzle box', False, 'It is a strange box. Perhaps it contains something \
inside of it? If only you could figure out a way to open it...')
basement.get('puzzle box').can_open = True
basement.can_go["north"] = True
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
kitchen.can_go["east"] = True

    
living_room = Room('living room', 1)
# in the living room is a couch, a table with drawers, and a TV set. You can only move
# west, back into the main hallway
living_room.add_item('couch', False, "It is a dusty couch. I wouldn't recommend sitting on it.")
living_room.get('couch').can_open = True                         
living_room.add_item('table', False, "It is a small wooden table with a drawer underneath.")
living_room.get('table').can_open = True
living_room.add_item('TV set', False, "It is a small television set from the 50s. You try to\
turn it on, but nothing happens. Bummer.")
living_room.can_go["west"] = True

    
main_hallway = Room('main landing hallway', 1)
    # no objects within this room. You can move in any direction.
    # North leads to the main landing stairway, South leads back outside, East leads to the
    # living room, and West leads to the kitchen
main_hallway.can_go["north"] = True
main_hallway.can_go["south"] = True
main_hallway.can_go["east"] = True
main_hallway.can_go["west"] = True

    
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
bedroom.can_go["east"] = True

    
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
bathroom.can_go["west"] = True

    
upper_hallway = Room('upper landing hallway', 2)
    # contains no objects. It is locked initially. Its key is located in the basement
    # puzzle box. You can move North to the upper stairway, West to the bedroom, or East
    # to the bathroom.
upper_hallway.locked = True
upper_hallway.can_go["north"] = True
upper_hallway.can_go["west"] = True
upper_hallway.can_go["east"] = True

    
attic = Room('attic', 3)
    # contains a single object: Mystery. It is locked initially. Its key is located somewhere
    # on floor 2. You can only move North, back down the stairs.
attic.locked = True
attic.add_item('???', True, "It is a mysterious object")
attic.can_go["north"] = True

