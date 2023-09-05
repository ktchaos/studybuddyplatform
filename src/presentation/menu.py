from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption

class Menu():
#mensagem padrao do sistema
    def getOption():
        print("Escolha a opcao:\n[1] Listar buddies.\n[2] Criar buddies.\n[3] Sair.")
        try: 
            option = int(input())
            if(option == 3):
                raise MenuExitOption
            elif(option in range(1,3)):
                return option
            raise MenuOpcaoInvalida
        except ValueError:
            raise MenuOpcaoInvalida