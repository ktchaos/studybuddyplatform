import socketserver
from util.exceptions.MenuOpcaoInvalidaException import MenuOpcaoInvalida
from util.exceptions.MenuExitOptionException import MenuExitOption
from presentation.menu import Menu
from infra.HttpServer import HttpServer

from presentation.studentPresentation import studentPresentation
from presentation.categoryPresentation import categoryPresentation

#from data.control.ManagerFacade import ManagerFacade
from presentation.roomPresentation import RoomPresentation

port = 8080

class ManagerController():
    
    def start():
        from data.control.ControllersFacade import ControllersFacade

        fa = ControllersFacade()

        while True:
            try:
                # Menu de opçoes
                option = Menu.getOptionsForManager()

                if option == 1:
                    fa.listBuddies()
                elif option == 2:
                    name, age, password = studentPresentation.getCreateData()
                    fa.createStudent(None, name, age, password)
                    # fa.createBuddyRemote()
                elif option == 3:
                    fa.listBuddies()
                    name = studentPresentation.selectStudent()
                    fa.selectStudent(name)
                    selection = Menu.getoptionsUpdateStudent()
                    update = studentPresentation.UpdateStudent(selection)
                    fa.updateStudent(name,update,selection)
                elif option == 4:
                    fa.backupStudent()
                elif option == 5:
                    title, description, categoryId = RoomPresentation.getCreateData()
                    fa.createRoom(None, title, description, categoryId)
                elif option == 6:
                    fa.listRooms()
                elif option == 7:
                    pass # Entrar na sala
                    #studentVm.enterRoom(room=roomVm.room)
                elif option == 8:
                    fa.listCategories()
                elif option == 9:
                    title, description = categoryPresentation.getCreateData()
                    fa.createCategory(None, title, description)
                elif option == 10:
                    fa.generateReport()
                elif option == 11:
                    # inicia servidor
                    with socketserver.TCPServer(("", port), HttpServer) as httpd:
                        print(f"Servidor rodando na porta {port}")
                        # Inicia o servidor e fica em execução até ser interrompido (Ctrl+C)
                        httpd.serve_forever()
            except (KeyboardInterrupt, MenuExitOption):
                fa.saveChanges()
                print("\nEncerrando...\n======= Study Buddy Platform =======")
                break
            except MenuOpcaoInvalida as exc:
                print(exc.message)
