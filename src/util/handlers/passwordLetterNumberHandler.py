from util.handlers.HandlerIF import Handler
from util.exceptions.PasswordException import passwordException

class PasswordLetterNumberHandler(Handler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, password):
        if not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
            raise passwordException("A senha deve conter letras e números.")
        return self.handleNext(password)
