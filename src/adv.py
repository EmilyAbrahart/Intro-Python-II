from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

options = '\nYour available options are:\n\n| [n] North | [e] East | [s] South | [w] West | ----- | [q] Quit |\n'
directions = {'n': 'north', 'e': 'east', 's': 'south', 'w': 'west'}
player1 = Player('Bob', room['outside'])

print('\n*.*.*. ADVENTURE GAME .*.*.*')
print(player1)
print(options)

selection = ''
while selection != 'q':

    selection = input(
        'Please choose which direction you would like to travel:')

    try:
        if selection == 'q':
            print('Thank you for playing Adventure Game!')
        elif selection == 'n':
            if player1.room.n_to:
                player1.room = player1.room.n_to
                print(player1)
            else:
                print('Oh no! You can\'t go that way...')
        elif selection == 'e':
            if player1.room.e_to:
                player1.room = player1.room.e_to
                print(player1)
            else:
                print('Oh no! You can\'t go that way...')
        elif selection == 's':
            if player1.room.s_to:
                player1.room = player1.room.s_to
                print(player1)
            else:
                print('\nOh no! You can\'t go that way...\n')
        elif selection == 'w':
            if player1.room.w_to:
                player1.room = player1.room.w_to
                print(player1)
            else:
                print('Oh no! You can\'t go that way...')   
        else:
            print('You didn\'t enter a valid option. Please try again.')
            print(options)
    except ValueError:
        print('Please choose one of the available options')
