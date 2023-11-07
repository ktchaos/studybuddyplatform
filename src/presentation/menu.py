from util.exceptions.MenuOpcaoInvalidaException import MenuOpcaoInvalida
from util.exceptions.MenuExitOptionException import MenuExitOption

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
            "Escolha a opcao:\n[1] Listar buddies.\n[2] Criar buddies.\n[3] Atualizar buddies.\n[4] Desfazer alteração de buddies.\n[5] Criar sala.\n[6] Listar salas.\n[7] Entrar na sala.\n[8] Listar categorias. \n[9] Criar categoria. \n[10] Gerar relatório.\n[11] Iniciar servidor.\n[12] Sair."
            )
        try: 
            option = int(input())
            if(option == 12):
                raise MenuExitOption
            elif(option in range(1,13)):
                return option
            raise MenuOpcaoInvalida
        except ValueError:
            raise MenuOpcaoInvalida
        

    def getoptionsUpdateStudent():
        print("[1] Atualizar nome.\n[2] Atualizar idade.\n[3] Atualizar senha.")
        option = int(input())
        return option