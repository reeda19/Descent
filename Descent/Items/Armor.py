from Item import Item
class Armor(Item):
    """armor class is subclass of item"""
    crit_decrease = 0 #decreases chance of critical hit on player
    damage_decrease = 0 #decreases amount of blood loss to player
    body_part = '' #helmet is head, chestplate is body, gauntlets are arms, boots are legs
    def __init__(self, name, crit_decrease, damage_decrease, body_part):
        self.crit_decrease = crit_decrease
        self.damage_decrease = damage_decrease
        self.body_part = body_part
        super(Armor, self).__init__(False, name) 