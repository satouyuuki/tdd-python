from .expression import Expression
from .money import Money
from .sum import Sum
from typing import cast

class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        sum: Sum = cast(Sum, source)
        amount: int = sum.augend._amount + sum.addend._amount
        return Money(amount, to)
