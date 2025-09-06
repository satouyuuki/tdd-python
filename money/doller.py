from .money import Money

class Doller(Money):
    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount=amount, currency=currency)

    def times(self, multiplier: int) -> 'Money':
        return Money.doller(self._amount * multiplier)
