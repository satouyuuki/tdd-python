from abc import ABC, abstractmethod

class Money(ABC):
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Money):
            return False
        return self._amount == obj._amount and self.__class__.__name__.__eq__(obj.__class__.__name__)

    @staticmethod
    def doller(amount: int) -> 'Money':
        from .doller import Doller
        return Doller(amount)

    @staticmethod
    def franc(amount: int) -> 'Money':
        from .franc import Franc
        return Franc(amount)

    @abstractmethod
    def times(self, multiplier: int) -> 'Money':
        pass

    @abstractmethod
    def currency(self) -> str:
        pass

