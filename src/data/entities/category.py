import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class Category:

    def __init__(self, id, title, description):
        from data.entities.room import Room

        self.title = title
        self.rooms: [Room] = []
    
    def printCategory(self):
        print(f'[Categoria {self.title}].')
        for room in self.rooms:
            room.printRoom()