
from player import Player
from data import room_data as room, options_data as options, item_data as item
from utils import pretty_print

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

welcome = '*.*.*. ADVENTURE GAME .*.*.*'
exitMessage = 'Thank you for playing Adventure Game!'
player1 = Player('Bob', room['outside'])

pretty_print(welcome)
pretty_print(*options.values())
pretty_print(player1.room.name, player1.room.description)

selection = ''

while selection != 'q':

    selection = input(
        '\nWhat would you like to do? ')

    selection_words = selection.split(' ')
    selection_word_length = len(selection_words)

    try:
        if selection_word_length == 1:
            if selection == 'q':
                pretty_print(exitMessage)
            elif selection in ['n', 'e', 's', 'w']:
                player1.travel(selection)
            elif selection == 'i':
                player1.show_inventory()
            elif selection == 'r':
                player1.room.show_items()
            elif selection == 'o':
                pretty_print(*options.values())
            else:
                pretty_print('You didn\'t enter a valid option. Please try again.')
                pretty_print(*options.values())
        elif selection_word_length == 2:
            if selection_words[0] == 'drop':
                player1.drop_item(selection_words[1])
            elif selection_words[0] == 'take':
                player1.take_item(selection_words[1])
            else:
                pretty_print('You didn\'t enter a valid option. Please try again.')
                pretty_print(*options.values())
    except ValueError:
        pretty_print('Please choose one of the available options')
