class Location(object):
    """describes and defines the contents of an individual location"""
    enemies = []
    connected_locations = [] # Should this be defined here or under Map.py?
    items = []
    description = ''
    special_actions = {}

    def __init__(self, name, enemies, connected_locations, items, description, special_actions):
       self.name=name
       self.enemies = enemies
       self.connected_locations = connected_locations
       self.items = items
       self.description = description
       self.special_actions = special_actions

    