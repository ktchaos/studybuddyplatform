from data.control.ManagerViewModel import ManagerViewModel
from data.control.StudentViewModel import StudentViewModel
from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption
from presentation.menu import Menu

def main():

    managerVm = ManagerViewModel(id=1, name="Gestor")

    while True:

        try:
            # Menu de opçoes
            option = Menu.getOption()

            if option == 1:
                # Lista usuarios
                managerVm.getBuddies()
            elif option == 2:
                # Pega informacoes para novo usuario
                studentVm = StudentViewModel()
                # incrementa e pega id do ultimo buddy salvo
                managerVm.incrementLastBuddyId()
                newStudent = studentVm.createAccount(managerVm.getLastBuddyId())
                # Salva na ManagerViewModel
                managerVm.saveBuddy(newStudent)
        except (KeyboardInterrupt, MenuExitOption): 
            print("\nEncerrando...\n======= Study Buddy Platform =======")
            break
        except MenuOpcaoInvalida as exc:
            print(exc.message)

 
main()
