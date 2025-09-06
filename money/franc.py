from .money import Money

class Franc(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount=amount, currency=currency)

    def times(self, multiplier: int) -> 'Money':
        return Money.franc(self._amount * multiplier)
