import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.room import Room
from data.entities.category import Category

class RoomAuthenticationError(Exception):
    def authenticate_name(self, title):
        if not title:
            raise RoomAuthenticationError("O título da sala não pode ser vazio.")
        if len(title) < 8:
            raise RoomAuthenticationError("O título precisa ter no mínimo 8 caracteres.")

class RoomViewModel:
    def __init__(self) -> None:
        super().__init__()

    def createRoom(self, id) -> Room:
        while True:
            try:
                print("Digite o título da sala:")
                title = input()
                authenticate = RoomAuthenticationError()
                authenticate.authenticate_name(title)
            except RoomAuthenticationError as error:
                print("Erro:", error)
                continue
            else:
                break
            
        print("Digite a descrição da sala:")
        description = input()

        createdRoom = Room(id=id, title=title, description=description, category=Category(id=1, title="test", description="test 2"))
        self.room = createdRoom
        return createdRoom
    