from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption

class Menu():
#mensagem padrao do sistema
    def getOptions():
        print("Escolha a opcao:\n[1] Login.\n[2] Sair.")
        try: 
            option = int(input())
            if(option == 2):
                raise MenuExitOption
            elif(option in range(1,3)):
                return option
            raise MenuOpcaoInvalida
        except ValueError:
            raise MenuOpcaoInvalida
        
    def getOptionsForBuddy():
        print(
            "Escolha a opcao:\n[1] Listar salas.\n[2] Listar categorias.\n[3] Criar sala.\n[4] Sair."
            )
        try: 
            option = int(input())
            if(option == 4):
                raise MenuExitOption
            elif(option in range(1,5)):
                return option
            raise MenuOpcaoInvalida
        except ValueError:
            raise MenuOpcaoInvalida

    def getOptionsForManager():
        print(
            "Escolha a opcao:\n[1] Listar buddies.\n[2] Criar buddies.\n[3] Criar sala.\n[4] Listar salas.\n[5] Entrar na sala.\n[6] Listar categorias. \n[7] Criar categoria. \n[8] Gerar relatório.\n[9] Iniciar servidor.\n[10] Sair."
            )
        try: 
            option = int(input())
            if(option == 10):
                raise MenuExitOption
            elif(option in range(1,11)):
                return option
            raise MenuOpcaoInvalida
        except ValueError:
            raise MenuOpcaoInvalida