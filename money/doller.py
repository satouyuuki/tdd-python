from .money import Money

class Doller(Money):
    def times(self, multiplier: int) -> 'Doller':
        return Doller(self._amount * multiplier)
