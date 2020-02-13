# Write a class to hold player information, e.g. what room they are in
# currently.

from utils import pretty_print


class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def travel(self, direction):
        next_room = self.room.get_next_room(direction)
        if next_room:
            self.room = next_room
            pretty_print(self.room.name, self.room.description)
        else:
            pretty_print('\nOh no! You can\'t go that way...\n')

    def take_item(self, item):
        for i in self.room.items:
            if item.lower() == i.name.lower():
                self.inventory.append(i)
                self.room.items.remove(i)
                pretty_print(
                    f'You have picked up the {i.name} in {self.room.name}. {i.name} has been added to your inventory.')

    def drop_item(self, item):
        for i in self.inventory:
            if item.lower() == i.name.lower():
                self.inventory.remove(i)
                self.room.items.append(i)
                pretty_print(
                    f'You have dropped the {i.name} in {self.room.name}. {i.name} has been removed from your inventory.')

    def show_inventory(self):
        if len(self.inventory) > 0:
            pretty_print('- - Inventory - -')
            for i in self.inventory:
                pretty_print(i.name, i.description)
        else:
            pretty_print("There are no items in your inventory.")

    def __str__(self):
        return f"{self.name} is currently in {self.room.name}"
