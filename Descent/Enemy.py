class Enemy(object):
    """Generic Enemy Template"""
    blood_amount = 0
    damage = 0
    attack_name = ''
    crit_chance  = 0
    name = ''

    def __init__(self, blood_amount, attack_name, crit_chance , name, damage):
        self.blood_amount = blood_amount  
        self.attack_name = attack_name
        self.crit_chance = crit_chance 
        self.name = name
        self.damage = damage # bleeding damage done over time. Should this be a set amount or a range?
    def attack(self):
        return self.crit_chance 