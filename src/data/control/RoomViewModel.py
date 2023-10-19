import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.room import Room
from data.entities.category import Category
from infra.HandleFile import HandleFile

class RoomViewModel:
    def __init__(self):
        self.currentRooms: [Room] = HandleFile().loadRooms()
        ## pega o id do ultimo buddy salvo  
        try:
            self.lastRoomId = self.currentRooms[-1].id
        except IndexError:
            self.lastRoomId = -1

    def createRoom(self, id, title, description, category: Category) -> Room:
        createdRoom = Room(id=id, title=title, description=description, category=category)
        self.room = createdRoom
        return createdRoom
    
    def save(self, room: Room):
        self.currentRooms.append(room)
        HandleFile().saveRooms(self.currentRooms)

    def getRooms(self):
        return self.currentRooms

    def getLastRoomId(self):
        return self.lastRoomId
    
    def incrementLastRoomId(self):
        self.lastRoomId += 1
    