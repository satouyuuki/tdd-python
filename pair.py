from typing import cast

# bankクラスでしか使わない内部クラスだからbankクラスに閉じ込めても良いかもしれない
class Pair:
    def __init__(self, frm: str, to: str) -> None:
        self._frm = frm
        self._to = to

    def __eq__(self, obj: object) -> bool:
        pair: Pair = cast(Pair, obj)
        return self._frm == pair._frm and self._to == pair._to

    def __hash__(self) -> int:
        return 0
