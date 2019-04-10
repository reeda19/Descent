class MapMod:

	'''
	A MapMod is an object that modifies the status of a Map object.
	
	There are a few different "mod types":
	1) 'move player' modtype results in the location of the player being moved.
	
	'''
	def __init__(self, modtype, **kwargs):
		self.type = modtype
		self.attrs = kwargs.items()

	def __getitem__(self, key):
		return self.attrs[key]

	def __setitem__(self, key, value):
		self.attrs[key] = value

	def __iter__(self):
		for key, value in self.attrs.items():
			yield (key, value)




	# going to work on this more later.