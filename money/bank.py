from .expression import Expression
from pair import Pair

class Bank:
    def __init__(self) -> None:
        self._rates: dict[Pair, int] = dict()

    def reduce(self, source: Expression, to: str) -> 'Money': # type: ignore
        return source.reduce(self, to)

    def addRate(self, frm: str, to: str, rate: int) -> None:
        self._rates[Pair(frm, to)] = rate

    def rate(self, frm: str, to: str) -> int:
        if (frm == to):
            return 1
        return self._rates[Pair(frm, to)]

