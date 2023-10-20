from .ManagerViewModel import ManagerViewModel
from .RoomViewModel import RoomViewModel
from .CategoryViewModel import CategoryViewModel
from .StudentViewModel import StudentViewModel
from .Login.LoginViewModel import LoginViewModel
from presentation.ManagerController import ManagerController
from presentation.BuddyController import BuddyController
from data.model.HTMLReport import HTMLReport
from data.model.PDFReport import PDFReport

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

        return cls._instance

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

    def login(self):
        print("Digite seu username:")
        username = input()
        print("Digite sua senha:")
        password = input()
        self.loginVm.currentBuddies = self.managerVm.currentBuddies
        (isManager, isLogged) = self.loginVm.authenticate(username, password)
        if isManager and isLogged:
            managerController = ManagerController()
            managerController.start()
        elif isLogged:
            buddyController = BuddyController()
            buddyController.start()
        else:
            print('-------------- Tente novamente --------------')
            

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
        