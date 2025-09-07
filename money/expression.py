from abc import ABC, abstractmethod

class Expression(ABC):

    @abstractmethod
    def reduce(self, to: str) -> 'Money': # type: ignore
        pass
