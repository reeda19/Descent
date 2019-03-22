class Player(object):
    """Defines player"""
    limbs = ['leftArm', 'rightArm', 'LeftLeg', 'rightLeg', 'head']
   # health = 100 will decide upon this later
    inventory = []
    actions = []
    location = []
    name = ''
    def __init__(self, name):
        self.name=name
