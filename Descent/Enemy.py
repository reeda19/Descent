from RiteOfPassage import RiteOfPassage
class Enemy(RiteOfPassage):
    """Generic Enemy Template
    Enemies can be considered a ROP in the fact that they block a player from using a certain pathway
    They are a subclass of ROP
    """
    blood_amount = 0
    damage = 0
    attack_name = ''
    crit_chance  = 0
    name = ''
    location_from = '' #Which pathway the enemy is blocking
    location_to = ''
    def __init__(self, blood_amount, attack_name, crit_chance , name, damage, location_from, location_to):
        self.blood_amount = blood_amount  
        self.attack_name = attack_name
        self.crit_chance = crit_chance 
        self.name = name
        self.damage = damage # bleeding damage done over time. Should this be a set amount or a range?
        self.location_from = location_from
        self.location_to = location_to
        super(Enemy, self).__init__(self.location_from, self.location_to) 
    def attack(self):
        return self.crit_chance 
