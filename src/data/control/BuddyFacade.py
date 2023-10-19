from .ManagerViewModel import ManagerViewModel
from .RoomViewModel import RoomViewModel
from .CategoryViewModel import CategoryViewModel
from .StudentViewModel import StudentViewModel
from .Login.LoginViewModel import LoginViewModel

class BuddyFacade:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BuddyFacade, cls).__new__(cls)
            cls._instance.managerVm = ManagerViewModel(id=1, name="Gestor")
            cls._instance.roomVm = RoomViewModel()
            cls._instance.categoryVm = CategoryViewModel()
            cls._instance.studentVm = StudentViewModel()
            cls._instance.loginVm = LoginViewModel()

        return cls._instance

    def listRooms(self):
        rooms = self.roomVm.getRooms()
        for room in rooms:
            room.print()

    def listCategories(self):
        categories = self.categoryVm.getCategories()
        for category in categories:
            category.print()
        
    def createRoom(self, id, title, description, categoryId):
        if id == None:
            id = self.roomVm.getLastRoomId() + 1
        category = self.categoryVm.getCategoryById(categoryId)
        createdRoom = self.roomVm.createRoom(id, title, description, category)
        self.roomVm.save(createdRoom)
        self.roomVm.incrementLastRoomId()

    def saveChanges(self):
        self.managerVm.updateChanges()