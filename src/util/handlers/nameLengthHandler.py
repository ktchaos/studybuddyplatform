from util.handlers.HandlerIF import Handler
from util.exceptions.ErrorNameException import ErrorName

class NameLengthHandler(Handler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, name):
        if len(name) > 12:
            raise ErrorName("O nome não pode ter mais de 12 caracteres.")   
        return self.handleNext(name)
        