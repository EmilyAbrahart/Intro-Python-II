from room import Room
from item import Item

options_data = {
    'title': '- - - Options - - -',
    'travel': '* Travel *',
    'travel_options': '| [n] North | [e] East | [s] South | [w] West |',
    'items': '* Items *',
    'items_options': '| [i] Show Inventory | [r] Room Items |',
    'other': '* Other *',
    'other_options': '| [o] Options | [q] Quit |'
}

item_data = {
    'sword': Item("Sword", "A plain old rusty sword"),
    'book': Item("Book", "It doesn't look like anyone has read this in a while..."),
    'bag': Item("Bag", "A small satchel."),
    'potion': Item("Potion", "A small bottle of glowing, green liquid."),
    'treasure': Item('Treasure', "Oooh... It's shiny....")
}
# Declare all the rooms

room_data = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

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