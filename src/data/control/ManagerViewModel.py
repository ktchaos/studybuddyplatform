import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.room import Room
from data.entities.manager import Manager
from infra.BuddyFile import BuddyFile
from infra.RoomFile import RoomFile

class ManagerViewModel:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.manager = Manager()
        self.currentBuddies = BuddyFile.loadBuddies()
        self.rooms: [Room] = []#RoomFile.loadRooms()
        ## pega o id do ultimo buddy salvo  
        try:
            self.LastBuddyId = self.currentBuddies[-1].id
        except IndexError:
            self.LastBuddyId = -1

    # Listar usuarios
    def getBuddies(self):
        for buddy in self.currentBuddies:
            buddy.printBuddy()

    # Salva novo usuario
    def saveBuddy(self, buddy):
        self.currentBuddies.append(buddy)
        BuddyFile.saveBuddies(self.currentBuddies)

    # Adiciona nova sala
    def addRoom(self, room):
        self.rooms.append(room)
        #RoomFile.addRooms(self.rooms)

     # Listar usuarios
    def getRooms(self):
        for room in self.rooms:
            room.printRoom()

    def getLastBuddyId(self):
        return self.LastBuddyId
    
    def incrementLastBuddyId(self):
        self.LastBuddyId += 1