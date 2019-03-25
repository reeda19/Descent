'''
GameMap.py is where all in-game locations are defined definitively.
This is akin to loa_map.py in Lawrence of Arabia.
All locations made in this file are loaded to the main Map
file by adding all the names to the list at the end.
'''

''' template

L1 = Location(
	enemies = 
	connected_locations,
	items,
	description,
	special_actions
	)

'''
from Location import Location

L1 = Location(
	enemies = [], 
	connected_locations=[],
	items =[],
	description = "sample description",
	special_actions = {}
	)
L2 = Location(
	enemies = [], 
	connected_locations=[],
	items =[],
	description = "sample description 2",
	special_actions = {}
	)

# location connections are still going to have to be designated down here, I guess.
L1.connected_locations = [L2]
L2.connected_locations = [L1]

# all_locations is special, because it is used to load the Map function.
all_locations = [L1]
