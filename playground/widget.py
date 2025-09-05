class Widget:
    def __init__(self, msg) -> None:
        self.w = 50
        self.h = 50
        print(msg)
    def resize(self, w, h) -> None:
        self.w = w
        self.h = h
    def size(self) -> tuple[int, int]:
        return (self.w, self.h)
