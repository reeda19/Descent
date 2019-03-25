import GameMap  
default_name = 'Xerxes' # what should the default name be?
                        #why do we need a default name? If no name is chosen, a random one is assigned from the list

class Player(object):
    """Defines player"""
    limbs = ['leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'head']
    inventory = []
    actions = []
    location = []
    name = ''

    def __init__(self, name = default_name):
        self.dead = False
        self.name = name
        self.location = GameMap.L1
    def getHealth(self):
        limbs = " ".join(str(x) for x in self.limbs)
        return limbs
