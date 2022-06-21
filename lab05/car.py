from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, size):
        self._size = size
         
    @property 
    def size(self):
        return self._size
    
    @abstractmethod
    def __str__(self):
        pass




