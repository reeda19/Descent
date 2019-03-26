import GameMap  

class Player(object):
    """Defines player"""
    limbs = ['leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'head']
    inventory = []
    actions = []
    location = []
    name = ''
    bloodAmount = 12.0 #measured in pints. If player is wounded, they lose blood over a period of time, then slowly start to regain it. Eating food helps regain blood quicker. 
    def __init__(self, name):
        self.dead = False
        self.name = name
        self.location = GameMap.B1
    def getHealth(self):
        limbs = " ".join(str(x) for x in self.limbs)
        health = 'Blood: '+ str(self.bloodAmount) + ' pints.\nLimbs: ' + limbs
        return health
