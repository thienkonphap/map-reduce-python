class Rope(ABC):
    def __init__(self,d):
        self.length = 0
    @abstractmethod
    def __getitem__(self,i):
        pass
    @abstractmethod
    def __add__(self,r):
        pass
    @abstractmethod
    def __str__(self):
        pass