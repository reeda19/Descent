from Item import Item
class Weapon(Item):
    """weapon class is subclass of item"""
    crit_chance = 0
    two_handed = False #One handed or two handed-->player with one hand cannot wield a two handed weapon
    def __init__(self, name, crit_chance, two_handed):
        self.crit_chance = crit_chance
        self.two_handed = two_handed
        super(Weapon, self).__init__(False, name) 
