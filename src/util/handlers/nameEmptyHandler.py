from util.handlers.HandlerIF import Handler
from util.exceptions.ErrorNameException import ErrorName

class NameEmptyHandler(Handler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, name):
        if not name:
            raise ErrorName("O nome não pode estar vazio.")
        return self.handleNext(name)
        