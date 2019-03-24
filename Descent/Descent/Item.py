import abc
class Item(abc.ABC):
    """defines an item that can be picked up and used by the player"""
    consumable = False
    name = ''
    use_aliases = []

    def __init__(self, consumable, name):
    	'''
		Explanation of Item class attrs:

		consumable (boolean) True if item can be destroyed in game (somehow), False otherwise.
		name (str) player name.
		use_aliases (dict)

    	'''
        self.consumable = consumable
        self.name = name

    @abc.abstractmethod
    def useItem():