from src.classes import Product


def test_init_product_1(product_1: Product) -> None:
    """
    Проверяем инициализацию класса Product
    """
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5
