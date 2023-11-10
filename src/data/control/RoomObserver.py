from abc import ABC, abstractmethod

class RoomObserver(ABC):
    @abstractmethod
    def update(self, room):
        pass