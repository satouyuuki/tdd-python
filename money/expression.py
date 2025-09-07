from abc import ABC, abstractmethod

class Expression(ABC):

    @abstractmethod
    def reduce(self, bank: 'Bank', to: str) -> 'Money': # type: ignore
        pass
