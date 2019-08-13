# Write a class to hold player information, e.g. what room they are in
# currently.

from Room import Room

class Player:
    def __init__(self, name, room, items, level, xp=[]):
        self.name = name
        self.room = room
        self.items = items
        self.level = level
        self.xp = xp
        self.score = 0


    def __str__(self):
        return self.items 