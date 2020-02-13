# Implement a class to hold room information. This should have name and
# description attributes.

from utils import pretty_print


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
            pretty_print('- - Room Items - -')
            for i in self.items:
                pretty_print(i.name, i.description)
        else:
            pretty_print("There are no items this room.")

    def __str__(self):
        return f"{self.name}\n{self.description}"
