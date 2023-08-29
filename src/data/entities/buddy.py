from abc import ABC, abstractmethod

# Classe abstrata representando os usuários do sistema
class Buddy(ABC):
    def __init__(self, id, name, age, avatar, interest_subject):
        self.id = id # armazena id unico do aluno
        self.name = name  # armazena nome
        self.age = age # idade
        self.avatar = avatar # ? photo perfil
        self.interest_subjects = interest_subject # armazena assuntos de interesse

    def printBuddy(self):
        print(f'[Buddy {self.id}] {self.name}, {self.age} anos.')