from .money import Money

class Doller(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount=amount, currency="USD")

    def times(self, multiplier: int) -> 'Money':
        return Doller(self._amount * multiplier)
