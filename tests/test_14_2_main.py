from src.classes import Category, Product


def test_new_init(product4: Product, category1: Category, output_new_init_class_test: str) -> None:
    """
    Тестируем новый способ инициализации класса Category
    """
    category1.add_product(product4)
    assert category1.products == output_new_init_class_test


def test_add_product(new_product_test_input_data: dict) -> None:
    new_product = Product.new_product(new_product_test_input_data)
    assert new_product.name == "Samsung Galaxy S23 Ultra"


def test_product_prise_setter(product4: 'Product') -> None:
    product4.price = 1000000.0
    assert product4.price == 1000000
