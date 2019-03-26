from Item import Item
class Weapon(Item):
    """weapon class is subclass of item"""
    critChance = 0
    twoHanded = False #One handed or two handed
    def __init__(self, name, critChance, twoHanded):
        self.critChance = critChance
        self.twoHanded = twoHanded
        super(Weapon, self).__init__(False, name) 
