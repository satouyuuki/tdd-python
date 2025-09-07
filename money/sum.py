from .expression import Expression
from .money import Money

class Sum(Expression):
    def __init__(self, augend, addend) -> None:
        self.augend: Money = augend
        self.addend: Money = addend
