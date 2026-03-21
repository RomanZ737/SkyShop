class PrintMixin:

    def __init__(self) -> None:
        super().__init__()
        print(repr(self))

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}({self.name}, {self.description}, "
                f"{self.price}, {self.quantity})")
