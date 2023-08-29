import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.manager import Manager

class ManagerViewModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.manager = Manager()
        self.currentBuddies = []

    # Listar usuarios
    def getBuddies(self):
        for buddy in self.currentBuddies:
            buddy.printBuddy()

    # Salva novo usuario
    def saveBuddy(self, buddy):
        self.currentBuddies.append(buddy)