from util.handlers.HandlerIF import Handler
from util.exceptions.ErrorNameException import ErrorName

class NameHasNumberHandler(Handler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, name):
        if not name.isalpha():
            raise ErrorName("O nome não pode conter números.") 
        return self.handleNext(name)
        