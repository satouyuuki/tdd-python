from .money import Money

class Franc(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount=amount, currency="CHF")

    def times(self, multiplier: int) -> 'Money':
        return Franc(self._amount * multiplier)
