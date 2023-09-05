import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.control.BuddyViewModel import BuddyViewModel
from data.entities.student import Student
from util.UserValidator import userValidator
from util.PasswordException import passwordException

class ErrorName(Exception):
    def authenticate_name(self, name):
        if not name:
            raise ErrorName("O nome não pode estar vazio.")
        if not name.isalpha():
            raise ErrorName("O nome não pode conter números.")
        if len(name) > 12:
            raise ErrorName("O nome não pode ter mais de 12 caracteres.")

class StudentViewModel(BuddyViewModel):
    def __init__(self) -> None:
        super().__init__()

    def createAccount(self, id) -> Student:
        while True:
            try:
                print("Digite seu nome:")
                name = input()
                authenticate = ErrorName()
                authenticate.authenticate_name(name)
            except ErrorName as error:
                print("Erro:", error)
                continue
            else:
                break
            
        print("Digite sua idade:")
        age = int(input())

        while True:
            print("Digite sua senha: ")
            password = input()

            validator = userValidator(password)
            try:
                validator.validatePassword()
                break
            except passwordException as e:
                print(f"Erro de validação de senha: {e}")
                print("Tente novamente.")

        createdStudent = Student(
            id=id,
            name=name,
            age=age,
            password=password,
            avatar="",
            interest_subject=[]
        )
        self.student = createdStudent
        return createdStudent
    