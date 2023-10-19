import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.buddy import Buddy

class Student(Buddy):
    def __init__(self, isLogged, remoteId, id, name, age, password, avatar, interest_subject, numberOfAccessesLastMonth):
        super().__init__(isLogged, remoteId, id, name, age, password, avatar, interest_subject, numberOfAccessesLastMonth)

    def printBuddy(self):
        # self.remoteId = f'local_id_{self.id}'
        print(f'[Student {self.id} {self.remoteId}] {self.name}, {self.age} anos.')

    # Função do Student para entrar em uma sala
    def enterRoom():
        pass