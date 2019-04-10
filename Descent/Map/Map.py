import Player
import GameMap
import GameROP
from Descent import protag
class Map(object):
	"""
	MAP object source.

	Map objects store and manage all data about the current game state.
	Players in the game are defined locally to it, as well as
	all instances of locations, including how they nodully connect to
	one another.

	Map is able to define rites of passages (i.e. in-game hinderances
	to moving around the map, such as a locked door).

	Because Map is a self-contained object that comprehensively contains
	all game data, it is possible that the Map object could later be
	used for save-load functionality.
	"""

	def __init__(self):
		self.locations = GameMap.all_locations #Defines every location in a list
		self.rites_of_passage = GameROP.all_rops #Defines every rite of passage in a list

	def move_player(self, new_location):
		for rop in self.rites_of_passage:
			if any(rop.trigger_rop(protag.location, new_location)):
			# this location requires us to trigger this rop
				rop.call_rop()