class Product:
    """
    Класс Продукт, который содержим общие сведения о продукте
    """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """
    Класс Категория, который содержит общие сведения о категориях товаров
    """
    name: str
    description: str
    products: list[Product]
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.product_count += len(products)
        Category.category_count += 1
