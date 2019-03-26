import Player
import GameMap
import GameROP
class Map(object):
	"""
	MAP object source.

	Map objects store and manage all data about the current game state.
	Players in the game are defined locally to it, as well as
	all instances of locations, including how they nodally connect to
	one another.

	Map is able to define rites of passages (i.e. in-game hinderances
	to moving around the map, such as a locked door).

	Because Map is a self-contained object that comprehensively contains
	all game data, it is possible that the Map object could later be
	used for save-load functionality.
	"""

	def __init__(self):
		self.protagonist = Player.Player('place_holder')
		self.locations = GameMap.all_locations
		self.rites_of_passage = GameROP.all_rops

	