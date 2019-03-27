class Location(object):
    """describes and defines the contents of an individual location"""
    connected_locations = [] # Should this be defined here or under Map.py?
    items = []
    description = ''
    special_actions = {}

    def __init__(self, name, items, description, special_actions):
        self.name = name
        self.items = items
        self.description = description
        self.special_actions = special_actions



    