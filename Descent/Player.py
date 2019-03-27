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
        self.location = GameMap.B1 #Starting location

    def getHealth(self):
        limbs = " ".join(str(x) for x in self.limbs)
        health = 'Blood: '+ str(self.bloodAmount) + ' pints.\nLimbs: ' + limbs
        return health

    def __contains__(self, item):
        return item in self.inventory

    def __iter__(self):
	    for item in self.inventory:
	        yield item

    def __len__(self):
        return len(self.inventory)

    def acceptModPacket(self, modpack):
        for key, value in modpack:
            if key in 'name':
                self.name = value
            elif key == 'location':
                self.location = value
            elif key == 'inventory remove':
                try:
                    self.inventory.remove(value)
                except ValueError:
                    pass
            elif key == 'inventory add':
                self.inventory.append(value)