from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption

class Menu():
#mensagem padrao do sistema
    def getOption():
        print(
            "Escolha a opcao:\n[1] Listar buddies.\n[2] Criar buddies.\n[3] Criar sala.\n[4] Listar salas.\n[5] Entrar na sala.\n[6] Listar categorias. \n[7] Criar categoria. \n[8] Login. \n[9] Iniciar servidor.\n[10] Sair."
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