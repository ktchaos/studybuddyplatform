from ManagerViewModel import ManagerViewModel
from StudentViewModel import StudentViewModel

class MenuOpcaoInvalida(Exception):
    "valor da opcao invalida"
    def __init__(self, message="valor da opcao invalida"):
        self.message = message
        super().__init__(self.message)

#mensagem padrao do sistema
def menu():
    print("Escolha a opcao:\n[1] Listar buddies.\n[2] Criar buddies.\n[3] Sair.")
    try: 
        option = int(input())
        if(option in range(1,4)):
            return option
        raise MenuOpcaoInvalida
    except ValueError:
        raise MenuOpcaoInvalida


def main():

    managerVm = ManagerViewModel(id=1, name="Gestor")

    while True:

        try:
            # Menu de opçoes
            option = menu()

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
            else:
                print("Encerrando...\n======= Study Buddy Platform =======")
                break
        except KeyboardInterrupt:
            print("\nEncerrando...\n======= Study Buddy Platform =======")
            break
        except MenuOpcaoInvalida as exc:
            print(exc.message)

 
main()
