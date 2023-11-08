from data.entities.student import Student

class MementoAtualizacao():
    
    def __init__(self):
        self.backup = Student()

    def setEstado(self, student: Student):
        self.backup = student

    def getEstado(self):
        return self.backup
