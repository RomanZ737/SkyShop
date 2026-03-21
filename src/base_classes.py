from abc import ABC, abstractmethod


class BaseClass(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, product_properties: dict) -> object:
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class BaseClassCategory(ABC):

    @abstractmethod
    def add_product(self, product: object) -> None:
        pass

    @abstractmethod
    def products(self) -> str:
        pass
