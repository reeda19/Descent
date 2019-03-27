'''
This is where all rites of passages are defined for the map.
'''

from RiteOfPassage import RiteOfPassage
from Enemy import Enemy
from GameMap import *
#Define enemies in ROP since they are considered Rites Of Passage?
troll = Enemy(
	blood_amount = 150, 
	attack_name = 'hit',
	crit_chance = 0.3 , 
	name = 'troll', 
	damage = 20, 
	location_from = C2, 
	location_to = C3
	)
R1 = RiteOfPassage(
	location_from = GameMap.B1,
	location_to = B2,
	description = 'sample' #need to define a way to get through a rite of passage
	)

# all_rops is used to load the main Map object.
all_rops = [R1]
