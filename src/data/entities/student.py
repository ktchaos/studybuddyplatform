from buddy import Buddy

class Student(Buddy):
    def __init__(self, id, nome, avatar):
        super().__init__(id, nome, avatar)
