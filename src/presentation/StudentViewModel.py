import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from BuddyViewModel import BuddyViewModel
from data.entities.student import Student

class StudentViewModel(BuddyViewModel):
    def __init__(self) -> None:
        super().__init__()

    def createAccount(self, id) -> Student:
        print("Digite seu nome:")
        name = input()
        print("Digite sua idade:")
        age = int(input())

        createdStudent = Student(
            id=id,
            name=name,
            age=age,
            avatar="",
            interest_subject=[]
        )
        self.student = createdStudent
        return createdStudent