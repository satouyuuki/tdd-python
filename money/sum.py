from .expression import Expression
from .money import Money
from .bank import Bank

class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self.augend: Expression = augend
        self.addend: Expression = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount: int = self.augend.reduce(bank, to)._amount + self.addend.reduce(bank, to)._amount
        return Money(amount, to)

    def plus(self, addend: Expression) -> 'Expression':
        return Sum(self, addend)
