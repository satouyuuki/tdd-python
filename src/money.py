class Doller:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> 'Doller':
        return Doller(self.amount * multiplier)

    def equals(self, object: 'Doller') -> bool:
        return True
