'''
This is where all rites of passages are defined for the map.
'''

from RiteOfPassage import RiteOfPassage
from GameMap import *

R1 = RiteOfPassage(
	location_from = B1,
	location_to = B2,
	description = 'sample'
	)

# all_rops is used to load the main Map object.
all_rops = [R1]