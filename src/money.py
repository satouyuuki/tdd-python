class Doller:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> 'Doller':
        return Doller(self._amount * multiplier)

    def equals(self, obj: object) -> bool:
        if not isinstance(obj, Doller):
            return False
        return self._amount == obj._amount
