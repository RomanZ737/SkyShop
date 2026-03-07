from src.classes import Product


def test_init_product_1(product_1: Product) -> None:
    """
    Проверяем инициализацию класса Product
    """
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


# def test_init_category(category_1: Category) -> None:
#     """
#     Проверяем инициализацию класса Category
#     """
#     assert category_1.name == "Смартфоны"
#     assert category_1.description == ("Смартфоны, как "
#                                       "средство не только "
#                                       "коммуникации, но и "
#                                       "получения дополнительных "
#                                       "функций для удобства жизни")
#     assert len(category_1.products) == 3
#     assert category_1.category_count == 1
#     assert category_1.product_count == 3
