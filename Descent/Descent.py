import Player
import Enemy
import Map
import Location
import random
HELP_STRING = """
       ~COMMANDS~  
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
            if name[0] in 'describe':
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
        elif keywords[0] in ['nesw senw', 'north', 'east', 'south', 'west', 'northeast', 'northwest', 'southeast', 'southwest']:
            #move player in that direction
            try:
                direction = keywords[0]
                protag.location = protag.location.connected_locations[direction]
                print("You travel using the path that is "+ direction_string_dict[direction] + '.')
                print(protag.location.description)
            except KeyError:
                try:
                    direction = keywords[0]
                    reverse_direction_dict = {v: k for k, v in direction_string_dict()} #used for translating northeast -> ne for GameMap
                    new_direction = reverse_direction_dict[direction]
                    protag.location = protag.location.connected_locations[new_direction]
                    print("You travel using the path that is "+ directions_string_dict[direction] + '.')
                    print(protag.location.description)
                except KeyError:
                        print ('You cannot go ' + direction + '.') #path does not exist
        else: # bogus string
            print(random.choice(RANDOM_BOGUS_STRINGS))
            print('Type \'help\' for available commands')

if __name__ == '__main__':
    main()
