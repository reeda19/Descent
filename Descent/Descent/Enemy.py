class Enemy(object):
    """Generic Enemy Template"""
    health = 0
    damage = 0
    attackName = ''
    critChance = 0
    name = ''
    def __init__(self, health, damage, attackName, critChance, name):
        self.health=health
        self.damage=damage
        self.attackName=attackName
        self.critChance=critChance
        self.name=name
    def attack():
        return self.damage