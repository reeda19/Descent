class Enemy(object):
    """Generic Enemy Template"""
    health = 0
    damage = 0
    attackName = ''
    critChance = 0
    name = ''
    def __init__(self, health, attackName, critChance, name):
        self.health=health #if players don't have health, should enemies? 
        self.attackName=attackName
        self.critChance=critChance
        self.name=name
    def attack(self):
        return self.critChance