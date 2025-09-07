from abc import ABC, abstractmethod

class Expression(ABC):

    @abstractmethod
    def reduce(self, bank: 'Bank', to: str) -> 'Money': # type: ignore
        pass

    @abstractmethod
    def plus(self, addend: 'Expression') -> 'Expression':
        pass

    @abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        pass
