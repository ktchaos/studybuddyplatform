
from util.PasswordException import passwordException

class userValidator:
    def __init__(self, password):
        self.password = password

    def validatePassword(self):
        try:
            self.validateLength()
            self.validateLetterNumber()
            self.validateMinNumber()
            return True
        except passwordException as e:
            raise e

    def validateLength(self):
        if not 8 <= len(self.password) <= 20:
            raise passwordException("A senha deve ter entre 8 e 20 caracteres.")

    def validateLetterNumber(self):
        if not any(c.isalpha() for c in self.password) or not any(c.isdigit() for c in self.password):
            raise passwordException("A senha deve conter letras e números.")

    def validateMinNumber(self):
        numeros = [c for c in self.password if c.isdigit()]
        if len(numeros) < 2:
            raise passwordException("A senha deve conter pelo menos 2 números.")