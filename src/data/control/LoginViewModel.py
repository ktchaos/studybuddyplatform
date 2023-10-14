import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from infra.factories.BuddyRemoteDataBaseFactory import BuddyRemoteDataBaseFactory
from data.entities.buddy import Buddy

class LoginViewModel:

    def __init__(self):
        self.currentUsername = ""
        self.currentPassword = ""
        self.currentBuddies: [Buddy] = []
        self.remoteDb = BuddyRemoteDataBaseFactory.makeDataBase()

    def authenticate(self, username, password):
        for buddy in self.currentBuddies:
            if buddy.name == username:
                if buddy.password == password:
                    print("Bem vindo!")
                else:
                    print("Credenciais incorretas")
            return
                    

        print("Usuário não encontrado, tente novamente")
            