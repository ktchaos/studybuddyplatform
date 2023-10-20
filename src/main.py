import socketserver
from util.exceptions.MenuOpcaoInvalidaException import MenuOpcaoInvalida
from util.exceptions.MenuExitOptionException import MenuExitOption
from presentation.menu import Menu

from data.control.ControllersFacade import ControllersFacade

def main():

    fa = ControllersFacade()

    while True:

        try:
            # Menu de opçoes
            option = Menu.getOptions()
            
            if option == 1:
                fa.login()
        except (KeyboardInterrupt, MenuExitOption):
            fa.saveChanges()
            print("\nEncerrando...\n======= Study Buddy Platform =======")
            break
        except MenuOpcaoInvalida as exc:
            print(exc.message)

 
main()
