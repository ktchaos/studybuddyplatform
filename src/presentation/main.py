from ManagerViewModel import ManagerViewModel
from StudentViewModel import StudentViewModel

#mensagem padrao do sistema
def menu():
    while True:
        print("Escolha a opcao:\n[1] Listar buddies.\n[2] Criar buddies.\n[3] Sair.")
        option = int(input())
        if(option in range(1,4)):
            return option
        print("Opcao invalida\n\n")


def main():

    managerVm = ManagerViewModel(id=1, name="Gestor")
    newId = 0 # Contador de ids 

    while True:
        # Menu de opçoes
        option = menu()

        if option == 1:
            # Lista usuarios
            managerVm.getBuddies()
        elif option == 2:
            # Pega informacoes para novo usuario
            studentVm = StudentViewModel()
            newStudent = studentVm.createAccount(newId)
            newId += 1
            # Salva na ManagerViewModel
            managerVm.saveBuddy(newStudent)
        else:
            break
    
main()