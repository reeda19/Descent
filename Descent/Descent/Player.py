default_name = 'Xerxes' # what should the default name be?

class Player(object):
    """Defines player"""
    limbs = ['leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'head']
    inventory = []
    actions = []
    location = []
    name = ''

    def __init__(self, name = default_name):
        self.name = name
    def getHealth(self):
        limbs = " ".join(str(x) for x in self.limbs)
        return limbs
