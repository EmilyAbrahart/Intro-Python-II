# Implement a class to hold room information. This should have name and
# description attributes.
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


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def get_next_room(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        else:
            return None

    def show_items(self):
        if self.items:
            for i in self.items:
                return prettyPrint(i)
        else:
            return "There are no items this room."

    def __str__(self):
            return f"{self.name}\n{self.description}"
