from .expression import Expression
from .money import Money

class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)

    def addRate(self, frm: str, to: str, rate: int) -> None:
        pass
