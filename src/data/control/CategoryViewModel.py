import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.category import Category
from infra.HandleFile import HandleFile

class CategoryViewModel:
    def __init__(self):
        self.currentCategories: [Category] = HandleFile().loadCategories()
        ## pega o id do ultimo buddy salvo  
        try:
            self.lastCategoryId = self.currentCategories[-1].id
        except IndexError:
            self.lastCategoryId = -1

    def createCategory(self, id, title, description) -> Category:
        createdCategory = Category(id=id, title=title, description=description)
        return createdCategory
    
    def save(self, category: Category):
        self.currentCategories.append(category)
        return HandleFile().saveCategories(self.currentCategories)
    
    def getLastCategoryId(self):
        return self.lastCategoryId
    
    def incrementLastCategoryId(self):
        self.lastCategoryId += 1
    
    # Listar categorias
    def getCategories(self):
        return self.currentCategories
    def getCategoryById(self, id):
        try:
            return list(filter(lambda category: category.id == id, self.currentCategories))[0]
        except IndexError:
            return 

    