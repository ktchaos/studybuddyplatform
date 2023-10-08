from .ManagerViewModel import ManagerViewModel
from .RoomViewModel import RoomViewModel
from .CategoryViewModel import CategoryViewModel
from .StudentViewModel import StudentViewModel

class ControllersFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ControllersFacade, cls).__new__(cls)
            cls._instance.managerVm = ManagerViewModel(id=1, name="Gestor")
            cls._instance.roomVm = RoomViewModel()
            cls._instance.categoryVm = CategoryViewModel()
            cls._instance.studentVm = StudentViewModel()

        return cls._instance

    def listBuddies(self):
        self.managerVm.getBuddies()

    def listRooms(self):
        self.managerVm.getRooms()

    def listCategories(self):
        self.categoryVm.getCategories()

    def createBuddie(self):
        # Pega informacoes para novo usuario
        #incrementa e pega id do ultimo buddy salvo
        self.managerVm.incrementLastBuddyId()
        newStudent = self.studentVm.createAccount(self.managerVm.getLastBuddyId())
        #Salva na ManagerViewModel
        self.managerVm.saveBuddy(newStudent)
        
    def createRoom(self, id):
        createdRoom = self.roomVm.createRoom(id)
        self.managerVm.addRoom(createdRoom)
  