import Player
import Enemy
import Map
import Location
import random
#COMMANDS WITH A * STILL NEED TO BE IMPLEMENTED....These also may not be in the final game if they are not necessary
HELP_STRING = """ 
       ~COMMANDS~     
Help - Displays possible commands
Get <object> - Picks up object
*Use <object> - Uses object
Drop <object> - Drops object
Inventory - Displays all items in your inventory
Look - Provides description of the roomC you're in
*Open <Object> - Opens object and reveals its contents 
*Inspect <Object> - Inspects object and provides a description  
*Talk <Person> - initiates a conversation with a person                     
N - Travels to the room that is North
E - Travels to the room that is East
S - Travels to the room that is South
W - Travels to the room that is West
*Compass - Shows available rooms you can travel to
*Attack - attacks an enemy
Health - displays your current health
"""
RANDOM_BOGUS_STRINGS=['Sorry, that didn\'t make sense', 'I do not understand that', 'That is not an available actions'] #If input is not an action
direction_string_dict = { #defines which user input leads to which direction
'n' : 'north',	
'e' : 'east',
's' : 'south',
'w' : 'west',
'ne' : 'northeast',
'se' : 'southeast',
'nw' : 'northwest',
'sw' : 'southwest'
}
names = {
    'zach' : 'zach description', #descriptions to be made by olivia
    'alex' : 'alex description', #Each character has a different storyline/plot
    'jack' : 'jack description',
    'froggy' : 'froggy description',
    'olivia' : 'olivia description'
    }
print("Choose a character: Zach, Alex, Jack, Froggy, Olivia:\nType \'describe <character>\' to see a character\'s description.")
def main():
    while True: #character selection
        name = input('>').lower().strip().split()
        try:
            if name[0] in ['describe']:
                if name[1] in [x.lower() for x in list(names.keys())]:
                     print(names[name[1]])
                else:
                    print("That is not an option")
            elif name[0] in [x.lower() for x in list(names.keys())]:
                print('You have chosen',name[0])
                protag = Player.Player(name[0])
                break
            else:
                print('That is not an option, sorry')
        except IndexError: #if no input, name is chosen randomly
            name = random.choice(list(names.keys()))
            print('You have chosen',name)
            protag = Player.Player(name)
            break
    introduction = '' #back story
    print(introduction)
    print(protag.location.description)
    while True:
        
        if protag.damage_per_turn>0 and protag.turns_taking_damage>0: #Decreases player blood amount if they are currently bleeding
            protag.blood_amount-=protag.damage_per_turn
            protag.turns_taking_damage-=1
            print('You lost',protag.damage_per_turn,'pints of blood. This will continue for',protag.turns_taking_damage,'more turns.')
            
        elif protag.blood_amount!=10.0: #If player is not at full health and they are not bleeding, blood increase at half a pint/turn. This may be subject to increase if the player eats food
            protag.blood_amount+=0.5
            
        user_input = input('>').lower().strip()
        keywords = [x.strip() for x in user_input.split()]
        if len(keywords) == 0: #prevents index out of range error
            continue
        elif keywords[0] in ['help']:
            print(HELP_STRING)
        elif keywords[0] in ['whoami']:
            print(protag.name) 
        elif keywords[0] in ['health']:
            print(protag.getHealth())
        elif keywords[0] in ['look']:
            print(protag.location.description)
        elif keywords[0] in 'nesw senw': #for player typing shorthand
            #move player in that direction
            try:
                direction = keywords[0]
                protag.location = protag.location.connected_locations[direction]
                print("You travel using the path that is "+ direction_string_dict[direction] + '.')
                print(protag.location.description)
            except KeyError:
                        print ('You cannot go that way.') #path does not exist
        elif keywords[0] in ['north', 'east', 'south', 'west', 'northeast', 'northwest', 'southeast', 'southwest']: #for player typing full direction
            try:
                direction = keywords[0]
                reverse_direction_dict = {v: k for k, v in direction_string_dict.items()} #used for translating northeast -> ne for GameMap
                new_direction = reverse_direction_dict[direction]
                protag.location = protag.location.connected_locations[new_direction]
                print("You travel using the path that is "+ direction_string_dict[new_direction] + '.')
                print(protag.location.description)
            except KeyError:
                        print ('You cannot go ' + direction + '.') #path does not exist
        elif keywords[0] in ['i', 'inventory', 'items']:
            if len(protag) == 0:
                print('You are holding nothing.')
            else:
                for i in protag:
                    print(i.name,'\n') #Prints name attribute of each item in player's inventory
        elif keywords[0] in ['get','grab']: # retreiving item from environment
            item = keywords[1]
            try:
                if item in [x.name.lower() for x in protag.location.items]: #Searches through the name attribitues for items, since they are objects
                    index = [x.name.lower() for x in protag.location.items].index(item)
                    itemName = protag.location.items[index]
                    protag.location.items.remove(itemName) #removes item from location and adds it to inventory
                    protag.inventory.append(itemName)
                    print ('You ' + keywords[0] + ' the ' + keywords[1] + '.')
                else:
                    print('That is not at this location.')

            except IndexError:
                print('You didn\'t say what you want to pick up')
        elif keywords[0] in ['drop']: # retrieving item from environment
            item = keywords[1]
            try:
                if item in [x.name.lower() for x in protag]: #Searches through the name attribitues for items, since they are objects
                    index = [x.name.lower() for x in protag].index(item)
                    itemName = protag.inventory[index]
                    protag.inventory.remove(itemName) #removes item from location and adds it to inventory
                    protag.location.items.append(itemName)
                    print ('You ' + keywords[0] + ' the ' + keywords[1] + '.')
                else:
                    print('You do not have ' + item + '.')
                
            except IndexError:
                print('You didn\'t say what you want to drop.')
        else: # bogus string
            print(random.choice(RANDOM_BOGUS_STRINGS))
            print('Type \'help\' for available commands')

if __name__ == '__main__':
    main()
