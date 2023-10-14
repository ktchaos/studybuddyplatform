import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.room import Room
from data.entities.manager import Manager

from infra.factories.BuddyLocalDataBaseFactory import BuddyLocalDataBaseFactory
from infra.factories.BuddyRemoteDataBaseFactory import BuddyRemoteDataBaseFactory

# from infra.RoomFile import RoomFile

class ManagerViewModel:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.manager = Manager()
        self.localDb = BuddyLocalDataBaseFactory.makeDataBase()
        self.remoteDb = BuddyRemoteDataBaseFactory.makeDataBase()
        self.currentBuddies = []
        self.loadBuddies()
        self.rooms: [Room] = []

        ## pega o id do ultimo buddy salvo
        # try:
        #     self.LastBuddyId = self.currentBuddies[-1].id
        # except IndexError:
        #     self.LastBuddyId = -1

    def loadBuddies(self):
        self.currentBuddies = self.remoteDb.loadBuddies()

    # Listar usuarios
    def gerarRelatorio(self):
        for buddy in self.currentBuddies:
            buddy.printBuddy()

    # Salva novo usuario
    def saveBuddy(self, buddy):
        self.currentBuddies.append(buddy)
        self.localDb.saveBuddies(self.currentBuddies)

    def saveBuddyRemote(self, buddy):
        self.currentBuddies.append(buddy)
        self.remoteDb.saveBuddies(self.currentBuddies)

    def saveChanges(self):
        self.localDb.saveBuddies(self.currentBuddies)

    def updateChanges(self):
        for buddy in self.currentBuddies:
            self.remoteDb.updateBuddyRemoteId(buddy.remoteId)

    # Adiciona nova sala
    def addRoom(self, room):
        self.rooms.append(room)

     # Listar usuarios
    def getRooms(self):
        for room in self.rooms:
            room.printRoom()

    def getLastBuddyId(self):
        return self.LastBuddyId
    
    def incrementLastBuddyId(self):
        self.LastBuddyId += 1
