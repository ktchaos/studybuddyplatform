from .ManagerViewModel import ManagerViewModel
from .RoomViewModel import RoomViewModel
from .CategoryViewModel import CategoryViewModel
from .StudentViewModel import StudentViewModel
from .Login.LoginViewModel import LoginViewModel
from .MementoAtualizacao import MementoAtualizacao
from presentation.ManagerController import ManagerController
from presentation.BuddyController import BuddyController
from data.model.HTMLReport import HTMLReport
from data.model.PDFReport import PDFReport
from .command.CommandIF import Command
from .command.LoginExternalCommand import LoginExternalCommand

class ControllersFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ControllersFacade, cls).__new__(cls)
            cls._instance.managerVm = ManagerViewModel(id=1, name="Gestor")
            cls._instance.roomVm = RoomViewModel()
            cls._instance.categoryVm = CategoryViewModel()
            cls._instance.studentVm = StudentViewModel()
            cls._instance.loginVm = LoginViewModel()
            cls._instance.memento = MementoAtualizacao()

        return cls._instance
    
    #funcao que executa o comado
    def invoker(self, c: Command):
        return c.execute()

    def login(self, username, password):
        #cria o comando
        command = LoginExternalCommand(self, username, password)
        #executa
        (isManager, isLogged) = self.invoker(command)
        return isManager, isLogged


    def listBuddies(self):
        students = self.studentVm.getStudents()
        for student in students:
            student.printBuddy()

    def listRooms(self):
        rooms = self.roomVm.getRooms()
        for room in rooms:
            room.print()

    def listCategories(self):
        categories = self.categoryVm.getCategories()
        for category in categories:
            category.print()

    def createBuddie(self):
        # Pega informacoes para novo usuario
        #incrementa e pega id do ultimo buddy salvo
        self.managerVm.incrementLastBuddyId()
        newStudent = self.studentVm.createAccount(self.managerVm.getLastBuddyId())
        #Salva na ManagerViewModel
        self.managerVm.saveBuddy(newStudent)

    def createStudent(self, id, name, age, password):
        if id == None:
            id = self.studentVm.getLastStudentId() + 1
            self.studentVm.incrementLastStudentId()
        newStudent = self.studentVm.create(id, name, age, password)
        self.studentVm.saveStudent(newStudent)

    def createCategory(self, id, title, description):
        if id == None:
            id = self.categoryVm.getLastCategoryId() + 1
        category = self.categoryVm.createCategory(id, title, description)
        self.categoryVm.save(category)
        self.categoryVm.incrementLastCategoryId()
        
    def createRoom(self, id, title, description, categoryId):
        if id == None:
            id = self.roomVm.getLastRoomId() + 1
        category = self.categoryVm.getCategoryById(categoryId)
        createdRoom = self.roomVm.createRoom(id, title, description, category)
        self.roomVm.save(createdRoom)
        self.roomVm.incrementLastRoomId()

    def createBuddyRemote(self):
        self.managerVm.incrementLastBuddyId()
        newStudent = self.studentVm.createAccount(self.managerVm.getLastBuddyId())
        self.managerVm.saveBuddyRemote(newStudent)            

    def saveChanges(self):
        self.managerVm.updateChanges()

    def createBuddyRemote(self):
        self.managerVm.incrementLastBuddyId()
        newStudent = self.studentVm.createAccount(self.managerVm.getLastBuddyId())
        self.managerVm.saveBuddyRemote(newStudent)

    def generateReport(self):
        htmlReport = HTMLReport()
        pdfReport = PDFReport()

        htmlReport.generateReport()
        pdfReport.generateReport()

    def saveChanges(self):
        self.managerVm.updateChanges()

    def selectStudent(self,name):
        students = self.studentVm.getStudents()
        for student in students:
            if(name == student.getName()):
                student.printBuddy()

    def updateStudent(self,name,update, selection):
        students = self.studentVm.getStudents()
        for student in students:
            if(name == student.getName()):
                backup = self.studentVm.copyStudent(student)
                self.memento.setEstado(backup)
                self.studentVm.UpdateStudent(student, update, selection)


    def backupStudent(self):
        backup = self.memento.getEstado()
        students = self.studentVm.getStudents()
        for student in students:
            if(backup.getId() == student.getId()):
                self.studentVm.backupStudent(student, backup)
