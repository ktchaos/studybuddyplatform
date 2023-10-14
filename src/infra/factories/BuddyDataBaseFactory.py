from abc import ABC, abstractmethod

class BuddyDataBaseFactory(ABC):
    @abstractmethod
    def makeDataBase():
        pass