class Enemy(object):
    """Generic Enemy Template"""
    health = 0
    damage = 0
    attack_name = ''
    crit_chance  = 0
    name = ''

    def __init__(self, health, attack_name, crit_chance , name):
        self.health = health #if players don't have health, should enemies? 
        self.attack_name = attack_name
        self.crit_chance = crit_chance 
        self.name = name
    def attack(self):
        return self.crit_chance 