from data.control.ManagerViewModel import ManagerViewModel
from data.control.StudentViewModel import StudentViewModel
from data.control.CategoryViewModel import CategoryViewModel
from data.control.RoomViewModel import RoomViewModel
from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption
from presentation.menu import Menu

def main():

    managerVm = ManagerViewModel(id=1, name="Gestor")
    roomVm = RoomViewModel()
    categoryVm = CategoryViewModel()

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
            elif option == 3:
                # Cria sala
                roomVm.createRoom(id=1)
            elif option == 4:
                # Lista salas
                managerVm.getRooms()
            elif option == 5:
                # Entrar na sala
                studentVm.enterRoom(room=roomVm.room)
            elif option == 6:
                # Listar categorias
                categoryVm.getCategories()
        except (KeyboardInterrupt, MenuExitOption): 
            print("\nEncerrando...\n======= Study Buddy Platform =======")
            break
        except MenuOpcaoInvalida as exc:
            print(exc.message)

 
main()
