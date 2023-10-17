import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from infra.factories.BuddyRemoteDataBaseFactory import BuddyRemoteDataBaseFactory
from data.entities.buddy import Buddy
from .AuthAdapter import AuthAdapter

class LoginViewModel:

    def __init__(self):
        self.currentUsername = ""
        self.currentPassword = ""
        self.currentBuddies: [Buddy] = []
        self.remoteDb = BuddyRemoteDataBaseFactory.makeDataBase()

    def authenticate(self, username, password):
        # Usando o adapter
        auth_type = 'local'  # ou 'firebase'
        auth = AuthAdapter(auth_type)

        try:
            auth.login(username, password)
            print('Autenticado com sucesso!')
        except Exception as e:
            print('Credenciais inválidas: ' + str(e))

        
            