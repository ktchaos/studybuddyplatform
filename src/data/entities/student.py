import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from data.entities.buddy import Buddy

class Student(Buddy):
    def __init__(self, id, name, age, avatar, interest_subject):
        super().__init__(id, name, age, avatar, interest_subject)

    def printBuddy(self):
        print(f'[Student {self.id}] {self.name}, {self.age} anos.')