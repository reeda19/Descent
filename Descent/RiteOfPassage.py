def null_function(_):
	pass

class RiteOfPassage:


	'''
	Rite of passages defines obstructions between two locations.
	By default in the game, travel is allowed between any two
	connected nodes. Only a rite of passage (should) inhibit
	travel between two locations.

	When involked, a rite of passage will return a MapMod object,
	describing what, if any, change to the game state must be made.

	The passage function defines what behavior should be exhibited
	when the rite of passage is involked.
	'''
	description = ''
	Map = ''
	def __init__(self, location_from,
	 location_to, 
	 passage_function = null_function,
	 description = ''
	 ):
		self.location_from = location_from
		self.location_to = location_to
		self.passage_function = passage_function

	def __call__(self, Map = ''):
		return self.passage_function(self.Map)

	def __str__(self):
		return self.description
