
from util.handlers.HandlerIF import Handler
from util.exceptions.ErrorNameException import ErrorName

class NameValidator:
    def __init__(self, handler: Handler):
        self.handler = handler

    def validateName(self, name):
        try:
            return self.handler.handle(name)
        except ErrorName as error:
            print(f"Erro de validação do nome: {error}")
    
    