class Weapon(Item):
    """weapon class is subclass of item"""
    critChance = ''
    twoHanded = False #One handed or two handed
    def __init__(self, name, critChance, twoHanded):
        self.critChance = critChance
        self.twoHanded = twoHanded
        super().__init__(False, name) 
