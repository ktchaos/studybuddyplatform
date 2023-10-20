import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

class Room:

    from data.entities.category import Category

    def __init__(self, id, title, description, category: Category):
        self.id = id
        self.title = title
        self.description = description
        self.buddiesInside = []
        self.category = category
    
    def print(self):
        print(f'[Sala {self.id}] - {self.title}, {self.description}.')

    def letStudentEnterRoom(self, buddy):
        self.buddiesInside.append(buddy)