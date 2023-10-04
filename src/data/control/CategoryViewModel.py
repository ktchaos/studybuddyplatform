import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.category import Category

class CategoryViewModel:
    def __init__(self) -> None:
        self.categories: [Category] = []

    def createCategory(self, id) -> Category:
        print("Digite o nome da categoria:")
        title = input()

        print("Digite a descrição da categoria")
        description = input()

        createdCategory = Category(id=id, title=title, description=description)
        self.categories = createdCategory
        return createdCategory
    
    # Listar categorias
    def getCategories(self):
        for category in self.categories:
            print(category)
    