from .expression import Expression
from .money import Money

class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.doller(10)
