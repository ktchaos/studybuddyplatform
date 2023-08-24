from abc import ABC, abstractmethod

# Classe abstrata representando os usuários do sistema
class Buddy(ABC):
    def __init__(self, id, name, avatar):
        self.id = id
        self.name = name
        self.avatar = avatar