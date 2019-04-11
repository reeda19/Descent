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
	when the rite of passage is invoked.
	
	The key boolean states whether a player has completed the passage_function or not.
	Defaults to false until the passage_function is completed.
	'''
	
	def __init__(self, location_from,
	 location_to, 
	 passage_function = null_function,
	 description = '',
	 unlock_desc = '',
	 key = False
	 ):
		self.location_from = location_from
		self.location_to = location_to
		self.passage_function = passage_function
		self.key = key
		self.description=description
		self.unlock_desc=unlock_desc
		
	def __call__(self, Map = ''):
		return self.passage_function(Map)

	def __str__(self):
		return self.description

		#returns true if parameters are the same as ROP's location
	def trigger_rop(self, location_from, location_to):
		return self.location_from == location_from and self.location_to == location_to
	
	def get_key(self):
		return self.key
	
	def unlock(self):
		return self.unlock_desc