class ErrorName(Exception):
    def authenticate_name(self, name):
        if not name:
            raise ErrorName("O nome não pode estar vazio.")
        if not name.isalpha():
            raise ErrorName("O nome não pode conter números.")
        if len(name) > 12:
            raise ErrorName("O nome não pode ter mais de 12 caracteres.")