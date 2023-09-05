from abc import ABC, abstractmethod

class BuddyViewModel(ABC):
    # função para criar usuario
    @abstractmethod
    def createAccount(self):
        pass
        