import abc
class Item(abc.ABC):
    """defines an item that can be picked up and used by the player"""
    consumable = False
    name = ''

    def __init__(self, consumable, name):
        self.consumable = consumable
        self.name = name
    @abc.abstractmethod
    def useItem():