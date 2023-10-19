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
        if username == 'managermaster' and password == 'mana123ger':
            return (True, True)
        self.currentBuddies = self.remoteDb.loadBuddies()
        for buddy in self.currentBuddies:
            if buddy.name == username:
                if buddy.password == password:
                    buddy.isLogged = True
                    print("Bem vindo!")
                    return (False, buddy.isLogged)
                else:
                    print("Credenciais incorretas.")

        print("Usuário não encontrado.")
        return (False, False)

    def logout(self):
        pass