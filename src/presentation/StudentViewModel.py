from BuddyViewModel import BuddyViewModel

class StudentViewModel(BuddyViewModel):
    def __init__(self) -> None:
        super().__init__()

    def createAccount(self, id):
        print("Digite seu nome:")
        name = input()
        print("Digite sua idade:")
        age = int(input())

        self.id = id
        self.name = name
        self.age = age

    def print(self):
         print(f'[user {self.id}] {self.name}, {self.age} anos.')