class Location(object):
    """describes and defines the contents of an individual location"""
    enemies = []
    connectedLocations = [] # Should this be defined here or under Map.py?
    items = []
    description = ''
    specialActions = {}
    def __init__(enemies, connectedLocations, items, description, specialActions):
        enemies=self.enemies
        connectedLocations=self.connectedLocations
        items=self.items
        description = self.description
        specialActionsactions=self.specialActions