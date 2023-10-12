import socketserver
from presentation.presentationExceptions import MenuOpcaoInvalida
from presentation.presentationExceptions import MenuExitOption
from presentation.menu import Menu
from presentation.test import Test
from infra.HttpServer import HttpServer

from data.control.ControllersFacade import ControllersFacade

port = 8080

def main():

    fa = ControllersFacade()

    while True:

        try:
            # Menu de opçoes
            option = Menu.getOption()

            if option == 1:
                fa.listBuddies()
            elif option == 2:
                fa.createBuddie()
            elif option == 3:
                fa.createRoom(id=1)
            elif option == 4:
                fa.listRooms()
            elif option == 5:
                pass # Entrar na sala
                #studentVm.enterRoom(room=roomVm.room)
            elif option == 6:
                fa.listCategories()
            elif option == 7:
                Test.runTest()
            elif option == 8:
                # inicia servidor
                with socketserver.TCPServer(("", port), HttpServer) as httpd:
                    print(f"Servidor rodando na porta {port}")
                    # Inicia o servidor e fica em execução até ser interrompido (Ctrl+C)
                    httpd.serve_forever()
        except (KeyboardInterrupt, MenuExitOption): 
            print("\nEncerrando...\n======= Study Buddy Platform =======")
            break
        except MenuOpcaoInvalida as exc:
            print(exc.message)

 
main()
