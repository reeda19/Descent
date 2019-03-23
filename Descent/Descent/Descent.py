import Player
import Enemy
import Map
import Location
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
Compass - Shows available rooms you can travel to
Attack - attacks an enemy
Health - displays your current health
'''

while(True):
    names = ['zach', 'alex', 'jack', 'froggy', 'olivia']
    name = input("Choose a character: Zach, Alex, Jack, Froggy, Olivia:\n>").lower().strip()
    if(name in names):
        print('hello,',name)
        break;
    else:
        print('That is not an option, sorry')
    protag = Player.Player(name)

while True:
    response = input('>').lower().strip()
    #test
    if(response.find('whoami')!=-1):
        print(protag.name) 
