import abc
class Item():
    """defines an item that can be picked up and used by the player"""
    consumable = False
    name = ''
    use_aliases = []

    def __init__(self, consumable, name):
        self.consumable = consumable
        self.name = name
        '''
		Explanation of Item class attrs:

		consumable (boolean) True if item can be destroyed in game (somehow), False otherwise.
		name (str) item name.
		use_aliases (dict)

    	'''


    @abc.abstractmethod
    def useItem(self): #abstract since every item will have a different use
        print('test')