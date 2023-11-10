from util.handlers.HandlerIF import Handler
from util.exceptions.PasswordException import passwordException

class PasswordLengthHandler(Handler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, password):
        if not 8 <= len(password) <= 20:
            raise passwordException("A senha deve ter entre 8 e 20 caracteres.")        
        return self.handleNext(password)
        