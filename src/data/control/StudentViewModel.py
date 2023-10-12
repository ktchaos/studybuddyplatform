import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.control.BuddyViewModel import BuddyViewModel
from data.entities.student import Student
from data.entities.room import Room
from util.PasswordValidator import PasswordValidator
from util.PasswordException import passwordException
from infra.HandleFile import HandleFile

class ErrorName(Exception):
    def authenticate_name(self, name):
        if not name:
            raise ErrorName("O nome não pode estar vazio.")
        if not name.isalpha():
            raise ErrorName("O nome não pode conter números.")
        if len(name) > 12:
            raise ErrorName("O nome não pode ter mais de 12 caracteres.")

class StudentViewModel():
    def __init__(self):
        self.currentStudents: [Student] = HandleFile().loadStudents()
        ## pega o id do ultimo buddy salvo  
        try:
            self.lastStudentId = self.currentStudents[-1].id
        except IndexError:
            self.lastStudentId = -1

    def create(self, id, name, age, password):
        try:
            authenticate = ErrorName()
            authenticate.authenticate_name(name)
        except ErrorName as error:
            print("Erro:", error)
        validator = PasswordValidator(password)
        try:
            validator = PasswordValidator(password)
            validator.validatePassword()
        except passwordException as e:
            print(f"Erro de validação de senha: {e}")
            print("Tente novamente.")
        #validate password
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
    
    def saveStudent(self, student: Student):
        self.currentStudents.append(student)
        HandleFile().saveStudents(self.currentStudents)

    def getStudents(self):
        return self.currentStudents
    
    def getLastStudentId(self):
        return self.lastStudentId
    
    def incrementLastStudentId(self):
        self.lastStudentId += 1
    
    def enterRoom(self, room: Room):
        room.letStudentEnterRoom(self.student)
    