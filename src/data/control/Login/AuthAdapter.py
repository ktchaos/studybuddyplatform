
from .LocalAuthentication import LocalAuthentication
from .FirebaseAuthentication import FirebaseAuthentication

# Adapter para a escolha entre autenticação Local e via Firebase
class AuthAdapter:
    def __init__(self, auth_type):
        if auth_type == 'local':
            self.authentication = LocalAuthentication()
        elif auth_type == 'firebase':
            self.authentication = FirebaseAuthentication()

    def login(self, username, password):
        return self.authentication.login(username, password)

    def logout(self):
        return self.authentication.logout()
