from typing import Any


class MyException(Exception):
    """Общий класс исключения для SkyShop"""

    def __init__(self, *args: Any, **kwargs: Any):
        self.message = args[0] if args else 'Неизвестная ошибка'

    def __str__(self: 'MyException') -> str:
        return self.message


class ZeroProductsException(MyException):
    """Класс исключения при нулевом количестве продуктов при создании объекта класса
        Product или Class"""

    def __init__(self, *args: Any, **kwargs: Any):
        self.message = args[0] if args else 'Товар с нулевым количеством не может быть добавлен'
