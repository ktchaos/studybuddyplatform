import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.control.BuddyViewModel import BuddyViewModel
from data.entities.student import Student
from data.entities.room import Room
from data.control.RoomObserver import RoomObserver

from util.handlers.passwordLetterNumberHandler import PasswordLetterNumberHandler
from util.handlers.passwordMinNumberHandler import PasswordMinNumberHandler
from util.handlers.passwordLengthHandler import PasswordLengthHandler
from util.handlers.nameHasNumberHandler import NameHasNumberHandler
from util.handlers.nameLengthHandler import NameLengthHandler
from util.handlers.nameEmptyHandler import NameEmptyHandler
from util.PasswordValidator import PasswordValidator
from util.NameValidator import NameValidator


from infra.factories.BuddyRemoteDataBaseFactory import BuddyRemoteDataBaseFactory
from infra.HandleFile import HandleFile


class StudentViewModel(RoomObserver):
    def __init__(self):
        #  CARREGAR REMOTAMENTE PARA EVITAR CONFLITO DE ARQUIVOS
        self.currentStudents: [Student] = []
        self.remoteDb = BuddyRemoteDataBaseFactory.makeDataBase()
        self.loadStudents()

        # self.currentStudents: [Student] = HandleFile().loadStudents()
        ## pega o id do ultimo buddy salvo  
        # try:
        #     self.lastStudentId = self.currentStudents[-1].id
        # except IndexError:
        #     self.lastStudentId = -1

    def loadStudents(self):
        self.currentStudents = self.remoteDb.loadBuddies()

    def create(self, id, name, age, password):
        # Criando os handlers do nome e definindo a ordem em que os critérios vão ser checados
        nameHandler = NameEmptyHandler()
        nameHandler.setNextHandler(NameHasNumberHandler())
        nameHandler.setNextHandler(NameLengthHandler())

        # Criando o validador do nome
        nameValidator = NameValidator(nameHandler)

        # Validando o nome
        nameValidator.validateName(name)

        # Criando os handlers da senha e definindo a ordem em que os critérios vão ser checados
        passwordHandler = PasswordLengthHandler()
        passwordHandler.setNextHandler(PasswordLetterNumberHandler())
        passwordHandler.setNextHandler(PasswordMinNumberHandler())

        # Criando o validador da senha
        passwordValidator = PasswordValidator(passwordHandler)

        # Validando a senha
        passwordValidator.validatePassword(password)

        createdStudent = Student(
            remoteId="",
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
    
    def enterRoom(self, roomVm, room: Room):
        room.letStudentEnterRoom(self.student)
        roomVm.addRoomObserver(self)
        roomVm.notifyRoomObservers(room)

    def update(self, room):
        print(f"O estudante {self.student.name} entrou na sala {room.title}")
    
    def UpdateStudent(self, student: Student, update, selection):
        if(selection == 1):
            student.name = update
        elif(selection == 2):
            student.age = int(update)
        elif(selection == 3):
            student.password = update

    def backupStudent(self, student: Student, backup: Student):
        student.name = backup.name
        student.age = backup.age
        student.password = student.password

    def copyStudent(self, student: Student):
        Backup = Student.__copy__(student)
        return Backup
