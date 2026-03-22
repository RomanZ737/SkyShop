from typing import Any

from src.base_classes import BaseClass, BaseClassCategory
from src.mixins_classes import PrintMixin


class Product(BaseClass, PrintMixin):
    """
    Класс Продукт, который содержим общие сведения о продукте
    """
    instances: list = []
    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.instances.append(self)
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> Any:
        """
        Проверяет, что продукт преналежит классу Product и производит слажение или возвращает ошибку.
        :param other: Эксемпляр класса Product
        :return: Возвращает сумму произведений цены и количества
        """
        if type(other) is not type(self):
            raise TypeError("Продукты разного типа нельзя складывать")
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, product_properties: dict) -> 'Product':
        new_instance = cls(
            product_properties['name'],
            product_properties['description'],
            product_properties['price'],
            product_properties['quantity']
        )
        for obj in cls.instances:
            if obj.name == product_properties['name']:
                obj.quantity += product_properties['quantity']
                if obj.__price < product_properties['price']:
                    obj.__price = product_properties['price']

        return new_instance

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif self.__price > price:
            request = input('Вы подтверждаете понижение цены, y/n? ')
            if request == 'y':
                self.__price = price
            else:
                print('Действие отменено')
        else:
            self.__price = price


class Category(BaseClassCategory):
    """
    Класс Категория, который содержит общие сведения о категориях товаров
    """
    name: str
    description: str
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def __str__(self) -> str:
        product_num = 0
        for item in self.__products:
            product_num += item.quantity
        return f"{self.name}, количество продуктов: {product_num} шт.\n"

    def add_product(self, product: object) -> None:
        if issubclass(type(product), Product):
            self.__products.append(product)
            Category.category_count += 1
        else:
            raise TypeError('невозможно добавить этот продукт')

    @property
    def products(self) -> str:
        result_list = ''
        for item in self.__products:
            result_list += f'{str(item)}\n'
        return result_list


class ProductIterator:
    """
    Принимает экземпляр класса Category
    Возвращает итератор объектов категории.
    """
    category: Category

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self: 'ProductIterator') -> 'ProductIterator':
        """
        Возвращает итератор
        """
        return self

    def __next__(self) -> str:
        """
        Возвращает следующее значение интератора
        """
        all_products_str = self.category.products
        count_symbol = all_products_str.count('\n')
        product_list = all_products_str.split('\n', maxsplit=count_symbol-1)
        print('Product list:', product_list)
        print(f'self.index: {self.index} < int(self.category.product_count) {product_list}')
        if self.index < len(product_list):
            product_item = product_list[self.index].replace('\n', '')
            self.index += 1
            return product_item
        else:
            raise StopIteration


class Smartphone(Product):
    """Класс для отдельной категории товаров - «Смартфон».
        Наследуется от класса Product
    """
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Класс для отдельной категории товаров - «Трава газонная».
        Наследуется от класса Product
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Order(BaseClassCategory):
    """
    Класс служит для создания заказов
    """

    ID = 1

    def __init__(self, products: list) -> None:
        self.order_num = self.ID
        self.__products = products
        Order.ID += 1

    def add_product(self, product: object) -> None:
        """
        Метод добавляет новый продукт в заказ
        """
        if issubclass(type(product), Product):
            self.__products.append(product)
        else:
            raise TypeError('невозможно добавить этот продукт')

    @property
    def total_price(self) -> Any:
        """
        Метод подсчитывает общую стоимость заказов
        """
        return len(self.__products) * self.__products[0].price

    @property
    def products(self) -> str:
        result_list = ''
        for item in self.__products:
            result_list += f'{str(item)}\n'
        return result_list
