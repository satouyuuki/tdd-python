from .expression import Expression
from .money import Money

class Sum(Expression):
    def __init__(self, augend, addend) -> None:
        self.augend: Money = augend
        self.addend: Money = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend._amount + self.addend._amount
        return Money(amount, to)
