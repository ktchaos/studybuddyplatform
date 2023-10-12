import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.room import Room
from data.entities.manager import Manager

class ManagerViewModel:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.manager = Manager()
        self.currentBuddies = []
        self.rooms: [Room] = []#RoomFile.loadRooms()
        ## pega o id do ultimo buddy salvo  
        try:
            self.LastBuddyId = self.currentBuddies[-1].id
        except IndexError:
            self.LastBuddyId = -1

    # Listar usuarios
    def gerarRelatorio(self):
        for buddy in self.currentBuddies:
            buddy.printBuddy()