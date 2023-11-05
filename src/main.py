import socketserver
from util.exceptions.MenuOpcaoInvalidaException import MenuOpcaoInvalida
from util.exceptions.MenuExitOptionException import MenuExitOption
from presentation.menu import Menu
from presentation.LoginPresentation import LoginPresentation
from presentation.BuddyController import BuddyController
from presentation.ManagerController import ManagerController
from data.control.ControllersFacade import ControllersFacade

def main():

    fa = ControllersFacade()

    while True:

        try:
            # Menu de opçoes
            option = Menu.getOptions()
            
            if option == 1:
                user, password = LoginPresentation.start()
                (isManager, isLogged) = fa.login(user, password)
                if isManager and isLogged:
                    ManagerController.start()
                elif isLogged:
                    BuddyController().start()
                else:
                    print('-------------- Tente novamente --------------')
        except (KeyboardInterrupt, MenuExitOption):
            fa.saveChanges()
            print("\nEncerrando...\n======= Study Buddy Platform =======")
            break
        except MenuOpcaoInvalida as exc:
            print(exc.message)

 
main()
