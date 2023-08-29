from buddy import Buddy

class Administrator(Buddy):
    def __init__(self, id, name, avatar, permissions):
        super().__init__(name, avatar)
        self.permissions = permissions

    # Função do ADM para criar sala
    def createRoom():
        pass