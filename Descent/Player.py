import GameMap

class Player(object):
    """Defines player"""
    limbs = ['leftArm', 'rightArm', 'leftLeg', 'rightLeg', 'head'] #limbst hat the player is still able to use
    inventory = []
    actions = [] #Is this needed?
    location = []
    armor = { #armor can be picked up like an item and equipped. Only one piece of armor per body part.
       'head' : '',
       'body':'', 
       'legs': '', 
       'arms':''
       }
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