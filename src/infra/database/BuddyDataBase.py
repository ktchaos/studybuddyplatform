from abc import ABC, abstractmethod

class BuddyDataBase(ABC):
    @abstractmethod
    def saveBuddies(self, buddies):
        pass

    @abstractmethod
    def loadBuddies(self):
        pass