
from util.handlers.HandlerIF import Handler
from util.exceptions.PasswordException import passwordException

class PasswordValidator:
    def __init__(self, handler: Handler):
        self.handler = handler

    def validatePassword(self, password):
        try:
            return self.handler.handle(password)
        except passwordException as error:
            print(f"Erro de validação de senha: {error}")
            print("Tente novamente.")
