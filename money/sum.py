from .expression import Expression
from .money import Money
from .bank import Bank

class Sum(Expression):
    def __init__(self, augend, addend) -> None:
        self.augend: Money = augend
        self.addend: Money = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount: int = self.augend._amount + self.addend._amount
        return Money(amount, to)
