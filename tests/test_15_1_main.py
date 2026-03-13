import pytest

from src.classes import Category, Product, ProductIterator


def test_product_str(product_1: Product, product4: Product) -> None:
    assert str(product_1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_add(product_1: Product, product4: Product) -> None:
    print(product_1)
    print(product4)
    print(product_1 + product4)
    assert str(product_1 + product4) == '1761000.0'


def test_iter_object(category1: Category) -> None:
    iterator = ProductIterator(category1)
    iter(iterator)
    assert iterator.index == 0
    assert next(iterator) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert next(iterator) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert next(iterator) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."

    with pytest.raises(StopIteration):
        next(iterator)


def test_category_str(category1: Category) -> None:
    assert str(category1) == 'Смартфоны, количество продуктов: 27 шт.\n'
