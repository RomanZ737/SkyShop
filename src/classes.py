class Product:
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


class Category:
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

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    @property
    def products(self) -> str:
        result_list = ''
        for item in self.__products:
            result_list += f"{item.name}, {item.price} руб. Остаток: {item.quantity} шт.\n"
        return result_list
