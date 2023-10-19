class RoomAuthenticationError(Exception):
    def authenticate_name(self, title):
        if not title:
            raise RoomAuthenticationError("O título da sala não pode ser vazio.")
        if len(title) < 8:
            raise RoomAuthenticationError("O título precisa ter no mínimo 8 caracteres.")