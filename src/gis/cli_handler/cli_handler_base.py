from abc import ABC, abstractmethod

class CliHandlerBase(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def execute(self, args):
        pass