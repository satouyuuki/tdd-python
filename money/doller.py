from .money import Money

class Doller(Money):
    def times(self, multiplier: int) -> 'Money':
        return Doller(self._amount * multiplier)
