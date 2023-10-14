from abc import ABC, abstractmethod

# Classe abstrata representando os usuários do sistema
class Buddy(ABC):
    def __init__(self, remoteId, id, name, age, password, avatar, interest_subject):
        self.remoteId = remoteId # id salvo no banco de dados remoto
        self.id = id # id unico
        self.name = name  # nome
        self.age = age # idade
        self.password = password # senha
        self.avatar = avatar # foto perfil
        self.interest_subjects = interest_subject # assuntos de interesse

    def printBuddy(self):
        print(f'[Buddy {self.id} {self.remoteId}] {self.name}, {self.age} anos.')