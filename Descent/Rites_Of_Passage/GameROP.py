'''
This is where all rites of passages are defined for the map.
'''
from Maps import GameMap
from .RiteOfPassage import RiteOfPassage
from .Enemy import Enemy

#Define enemies in ROP since they are considered Rites Of Passage?
troll = Enemy(
	blood_amount = 150, 
	attack_name = 'hit',
	crit_chance = 0.3 , 
	name = 'troll', 
	damage = 20, 
	location_from = GameMap.C2, 
	location_to = GameMap.C3
	)
R1 = RiteOfPassage(
	location_from = GameMap.B1,
	location_to = GameMap.B2,
	description = 'ROP encountered', #need to define a way to get through a rite of passage
	unlock_desc = 'ROP unlocked'
	)

# all_rops is used to load the main Map object.
all_rops = [R1, troll]
