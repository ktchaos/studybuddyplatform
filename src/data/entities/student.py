import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.buddy import Buddy

class Student(Buddy):
    def __init__(self, isLogged = None, remoteId = None, id = None, name = None, age = None, password = None, avatar = None, interest_subject = None, numberOfAccessesLastMonth = None):
        super().__init__(isLogged, remoteId, id, name, age, password, avatar, interest_subject, numberOfAccessesLastMonth)

     
    def __copy__(self):
        # Cria uma nova instância da classe com o mesmo valor
        nova_instancia = Student(self.isLogged, self.remoteId ,self.id, self.name, self.age, self.password, self.avatar, self.interest_subjects, self.numberOfAccessesLastMonth)
        return nova_instancia
    
    
    def printBuddy(self):
        # self.remoteId = f'local_id_{self.id}'
        print(f'[Student {self.id} {self.remoteId}] {self.name}, {self.age} anos.')

    # Função do Student para entrar em uma sala
    def enterRoom():
        pass

    def getName(self):
        return self.name
    
    def getId(self):
        return self.id