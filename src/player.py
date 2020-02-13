# Write a class to hold player information, e.g. what room they are in
# currently.
from textwrap import wrap

def prettyPrint(content):
    width = 50

    print('\n+-' + '-' * width + '-+')

    for line in wrap(content.name, width):
        print('| {0:^{1}} |'.format(line, width))

    print('+-' + '-'*(width) + '-+')

    for line in wrap(content.description, width):
        print('| {0:^{1}} |'.format(line, width))

    print('+-' + '-'*(width) + '-+\n')


class Player:
    def __init__(self, name, room, inventory=None):
        self.name = name
        self.room = room
        self.inventory = inventory

    def travel(self, direction):
      next_room = self.room.get_next_room(direction)
      if next_room:
        self.room = next_room
        print(f"{self.name} is currently in {self.room}")
      else:
        print('\nOh no! You can\'t go that way...\n')

    def take_item(self, item):
      self.inventory.append(item)
    
    def drop_item(self, item):
      self.inventory.remove(item)

    def show_inventory(self):
      if self.inventory and len(self.inventory) > 0:
        for i in self.inventory:
          return prettyPrint(i)
      else:
        return "There are no items in your inventory"

    def __str__(self):
        return f"{self.name} is currently in {self.room}"

