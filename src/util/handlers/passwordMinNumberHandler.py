from util.handlers.HandlerIF import Handler
from util.exceptions.PasswordException import passwordException

class PasswordMinNumberHandler(Handler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, password):
        numeros = [c for c in password if c.isdigit()]
        if len(numeros) < 2:
            raise passwordException("A senha deve conter pelo menos 2 números.")
        return self.handleNext(password)
