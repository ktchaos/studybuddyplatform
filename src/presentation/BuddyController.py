import socketserver
from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption
from presentation.menu import Menu

from presentation.roomPresentation import RoomPresentation
from data.control.BuddyFacade import BuddyFacade

class BuddyController():
    def start(self):
        fa = BuddyFacade()
        while True:
            try:
                # Menu de opçoes
                option = Menu.getOptionsForBuddy()

                if option == 1:
                    fa.listRooms()
                elif option == 2:
                    fa.listCategories()
                elif option == 3:
                    title, description, categoryId = RoomPresentation.getCreateData()
                    fa.createRoom(None, title, description, categoryId)
            except (KeyboardInterrupt, MenuExitOption):
                fa.saveChanges()
                print("\nEncerrando...\n======= Study Buddy Platform =======")
                break
            except MenuOpcaoInvalida as exc:
                print(exc.message)
