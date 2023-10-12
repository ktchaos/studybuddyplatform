from data.control.ControllersFacade import ControllersFacade
class RoomPresentation():
    def getCreateData():
        fa = ControllersFacade()
        print("Digite o nome da sala:")
        title = input()
        print("Digite a descrição da sala:")
        description = input()
        print("Esclha a categoria da sala:")
        fa.listCategories()
        categoryId = int(input())
        return title, description, categoryId