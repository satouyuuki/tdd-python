from .expression import Expression
from .bank import Bank

class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount = amount
        self._currency = currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Money') -> 'Expression':
        from .sum import Sum
        return Sum(self, addend)

    def currency(self) -> str:
        return self._currency

    def reduce(self, bank: Bank, to: str) -> 'Money':
        rate: int =  bank.rate(self._currency, to)
        return Money(int(self._amount / rate), to)

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Money):
            return False
        return self._amount == obj._amount and self._currency == obj._currency

    # str()はどういう時に使う?
    # def __str__(self) -> str:
    # toString()の等価
    def __repr__(self) -> str:
        return f"Money(amount='{self._amount}', currency='{self._currency}')"

    @staticmethod
    def doller(amount: int) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, "CHF")
