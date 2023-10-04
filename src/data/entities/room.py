import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.buddy import Buddy
from data.entities.category import Category

class Room:
    def __init__(self, id, title, description, category: Category):
        self.id = id
        self.title = title
        self.description = description
        self.buddiesInside = []
        self.category = category
    
    def printRoom(self):
        print(f'[Sala {self.id}] - {self.title}, {self.description}.')

    def letStudentEnterRoom(self, buddy):
        self.buddiesInside.append(buddy)