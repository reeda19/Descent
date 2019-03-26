'''
GameMap.py is where all in-game locations are defined definitively.
This is akin to loa_map.py in Lawrence of Arabia.
All locations made in this file are loaded to the main Map
file by adding all the names to the list at the end.
'''

''' template

B1 = Location(
	name = '',
	enemies = [],
	items = [],
	description = '',
	special_actions = {}
	)

'''


'''***KEY***
Level names that start with...
B designate starting/beginner area
C are cave areas
L is lake
S is second summit
(add more as game goes on)
'''
from Location import Location

B1 = Location(
    name = 'Summit',
	enemies = [], 
	items =[],
	description = "You are at the top of the mountain. There is a a path to the southeast and a path to the southwest",
	special_actions = {}
	)
B2 = Location(
    name = 'Rocky Ridge',
    enemies = [], 
	items =[],
	description = "You approach a rocky cliffside. Branching off, there is a path to the east, a path that continues southwest, and a path leading up northeast.",
	special_actions = {}
	)
B3 = Location(
	name = 'Crossroads',
	enemies = [],
	items = [],
	description = 'There is a crossroads ahead of you, with a dingy sign. The letters are faded and unreadable. The paths go west, northwest, and southeast.',
	special_actions = {}
	)
	
# location connections are still going to have to be designated down here, I guess.
B1.connected_locations = {'se':B2, 'sw': B2}
B2.connected_locations = {'ne':B1, 'e': B3} #'sw': C2 (troll den/cave enterance)
B3.connected_locations = {'nw':B1, 'w' : B2} # 'se' :C1 (cave enterance)

# all_locations is special, because it is used to load the Map function.
all_locations = [B1, B2, B3]
