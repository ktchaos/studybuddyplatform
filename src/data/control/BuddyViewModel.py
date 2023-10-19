from abc import ABC, abstractmethod

class BuddyViewModel(ABC):
    # função para criar usuario
    @abstractmethod
    def create(self):
        pass
        