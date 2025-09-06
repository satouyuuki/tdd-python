class Money:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Money):
            return False
        return self._amount == obj._amount and self.__class__.__name__.__eq__(obj.__class__.__name__)
