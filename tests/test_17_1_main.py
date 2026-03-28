import pytest

from src.classes import Category, Order, Product


def test_zero_product_number() -> None:
    """
    Проверям условие "не нулевое количество продуктов" при добавлении объекта класса Product
    """
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price(category1: 'Category') -> None:
    """
    Проверяем метод класса moddle_price
    """
    assert category1.middle_price() == 140333.33


def test_middle_price_zero_division() -> None:
    """
    Проверка нулевого количества товаров в категории
    """
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0


def test_order_zero_product_number() -> None:
    """
    Проверка нулевого количества товаров в заказе
    """
    with pytest.raises(ValueError):
        product_5 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 0)
        Order([product_5])
