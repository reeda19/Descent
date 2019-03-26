import Player
import Enemy
import Map
import Location
import random
''' ~COMMANDS~  
Help - Displays possible commands
Get <object> - Picks up object
Use <object> - Uses object
Drop <object> - Drops object
Inventory - Displays all items in your inventory
Look - Provides description of the roomC you're in
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
names = {
    'zach' : 'zach description', #descriptions to be made by olivia
    'alex' : 'alex description',
    'jack' : 'jack description',
    'froggy' : 'froggy description',
    'olivia' : 'olivia description'
    }
print("Choose a character: Zach, Alex, Jack, Froggy, Olivia:\nType \'describe <character>\' to see a characters description.")

def main():
    while True: #character selection
        name = input('>').lower().strip().split()
        try:
            if name[0] in 'describe':
                print(names[name[1]])
            elif name[0] in names:
                print('You have chosen',name[0])
                protag = Player.Player(name[0])
                break
            else:
                print('That is not an option, sorry')
        except IndexError: #no input
            name = random.choice(list(names.keys()))
            print('You have chosen',name)
            protag = Player.Player(name)
            break
    while True:
        user_input = input('>').lower().strip()
        keywords = user_input.split()
        if len(keywords) == 0: #prevents index out of range error
            continue
        if user_input.find('whoami')!=-1:
            print(protag.name) 
        if user_input.find('health')!=-1:
            print('limbs:',protag.getHealth())
        if keywords[0] in 'look':
            print(protag.location.description)
if __name__ == '__main__':
	main()