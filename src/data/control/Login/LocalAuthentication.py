from .Authentication import Authentication

from infra.factories.BuddyRemoteDataBaseFactory import BuddyRemoteDataBaseFactory
from data.entities.buddy import Buddy

# Autenticação local
class LocalAuthentication(Authentication):
    def __init__(self):
        self.currentUsername = ""
        self.currentPassword = ""
        self.currentBuddies: [Buddy] = []
        self.remoteDb = BuddyRemoteDataBaseFactory.makeDataBase()

    def login(self, username, password):
        for buddy in self.currentBuddies:
            if buddy.name == username:
                if buddy.password == password:
                    print("Bem vindo!")
                else:
                    print("Credenciais incorretas.")
            else:
                print("Usuário não encontrado, tente novamente.")

    def logout(self):
        pass