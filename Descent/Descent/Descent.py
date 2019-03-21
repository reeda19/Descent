from Player import Player
import Enemy

''' ~COMMANDS~
Help - Displays possible commands
Get <object> - Picks up object
Use <object> - Uses object
Drop <object> - Drops object
Inventory - Displays all items in your inventory
Look - Provides description of the room you're in
Open <Object> - Opens object and reveals its contents
Inspect <Object> - Inspects object and provides a description
Talk <Person> - initiates a conversation with a person
N - Travels to the room that is North
E - Travels to the room that is East
S - Travels to the room that is South
W - Travels to the room that is West
Compass - Shows available rooms you can travel to'''
name = input('what is your name? ')
protag = Player(name)
while True:
    response = input('>')
