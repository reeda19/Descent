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
	descriptions,
	special_actions
	)

'''
import Location

L1 = Location(
	description = 'sample1'
	)
L2 = Location(
	description = 'samle2',
	)

# location connections are still going to have to be designated down here, I guess.
L1.connected_locations = [L2]
L2.connected_locations = [L1]

# all_locations is special, because it is used to load the Map function.
all_locations = [L1]