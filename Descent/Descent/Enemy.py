class Enemy(object):
    """Generic Enemy Template"""
    health = 0
    damage = 0
    attackName = ''
    critChance = 0
    name = ''
    def __init__(self, health, damage, attackName, critChance, name):
        health=self.health
        damage = self.damage
        attackName=self.attackName
        critChance = self.critChance
        name = self.name
    def attack():
        return damage