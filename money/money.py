class Money:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Money):
            return False
        return self._amount == obj._amount
