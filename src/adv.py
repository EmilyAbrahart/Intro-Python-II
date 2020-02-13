from textwrap import wrap
from room import Room
from player import Player
from item import Item

item = {
    'sword': Item("Sword", "A plain old rusty sword"),
    'book': Item("Book", "It doesn't look like anyone has read this in a while..."),
    'bag': Item("Bag", "A small satchel."),
    'potion': Item("Potion", "A small bottle of glowing, green liquid."),
    'treasure': Item('Treasure', "Oooh... It's shiny....")
}
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

# Add items to rooms
room['foyer'].items = [item['sword'], item['potion'], item['book']]
room['overlook'].items = [item['book'], item['potion']]
room['narrow'].items = [item['bag']]
room['treasure'].items = [item['treasure']]

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

options = '\nYour available options are:\n\nTravel:\n |[n] North | [e] East | [s] South | [w] West |\n\nItems:\n| [i] Show Inventory | [r] Room Items |\n\n| [q] Quit |\n'
directions = {'n': 'north', 'e': 'east', 's': 'south', 'w': 'west'}
welcome = '\n*.*.*. ADVENTURE GAME .*.*.*'
exitMessage = 'Thank you for playing Adventure Game!'
player1 = Player('Bob', room['outside'])

print(welcome)
print(player1)
print(options)


selection = ''
while selection != 'q':

    selection = input(
        'What would you like to do? ')

    try:
        if selection == 'q':
            print(exitMessage)
        elif selection in ['n', 'e', 's', 'w']:
            player1.travel(selection)
        elif selection == 'i':
            print(player1.show_inventory())
        elif selection == 'r':
            print(player1.room.show_items())
        else:
            print('You didn\'t enter a valid option. Please try again.')
            print(options)
    except ValueError:
        print('Please choose one of the available options')
