#
# TEXT-BASED ADVENTURE GAME
#
# CODEBREAKERS 2018
#

#
# player_class.py
#
# contains player class
#

import rooms

class Player: 
    
    name = ""
    current_room = rooms.outside
    inventory = []
    
    def __init__(self, name):
        self.name = name

   
