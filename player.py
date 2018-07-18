#
# TEXT-BASED ADVENTURE GAME
#
# CODEBREAKERS 2018
#
#





# Player class -- initialized upon starting the game

class Player(object):
    
    name = ""
    current_room = "outside"
    inventory = []
    
    def __init__(self, name):
        self.name = name
