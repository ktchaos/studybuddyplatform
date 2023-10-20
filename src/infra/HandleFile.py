import pickle

class HandleFile():
    #handle students file
    def loadStudents(self):
        return self.loadFile("students.bin")
    def saveStudents(self, students):
        return self.saveToFile("students.bin", students)
    
    #handle categories file
    def loadCategories(self):
        return self.loadFile("categories.bin")
    def saveCategories(self, categories):
        return self.saveToFile("categories.bin", categories)
    
    #handle rooms file
    def loadRooms(self):
        return self.loadFile("rooms.bin")
    def saveRooms(self, rooms):
        return self.saveToFile("rooms.bin", rooms)
       
    
    def loadFile(self, fileName):
        try:
            with open(f'./src/infra/saveLocalData/{fileName}', 'rb') as fp:
                content = pickle.load(fp)
                return content
        except FileNotFoundError:
            # se o arquivo nao existe, retorna uma lista vazia
            print('Arquivo nao encontrado.')
            return []
    def saveToFile(self, fileName, content):
        try:
            # salva a lista atualizada no arquivo
            with open(f'./src/infra/saveLocalData/{fileName}', 'wb') as fp:
                pickle.dump(content, fp)
        except FileNotFoundError:
            print('Erro ao salvar. Arquivo nao encontrado.')