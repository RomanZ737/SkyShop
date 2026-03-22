import pytest

from src.classes import Category, LawnGrass, Smartphone


def test_init_smartphone_product(samsung_1_product: "Smartphone") -> None:
    """
    Тест инициализации дочернего класса Smartphone
    """
    assert samsung_1_product.name == "Samsung Galaxy S23 Ultra"
    assert samsung_1_product.description == "256GB, Серый цвет, 200MP камера"
    assert samsung_1_product.price == 180000.0
    assert samsung_1_product.quantity == 5
    assert samsung_1_product.efficiency == 95.5
    assert samsung_1_product.model == "S23 Ultra"
    assert samsung_1_product.memory == 256
    assert samsung_1_product.color == "Серый"


def test_init_lawngrass_product(lawngrass_1_product: "LawnGrass") -> None:
    """
    Тест инициализации дочернего класса Smartphone
    """
    assert lawngrass_1_product.name == "Газонная трава"
    assert lawngrass_1_product.description == "Элитная трава для газона"
    assert lawngrass_1_product.price == 500.0
    assert lawngrass_1_product.quantity == 20
    assert lawngrass_1_product.country == "Россия"
    assert lawngrass_1_product.germination_period == "7 дней"
    assert lawngrass_1_product.color == "Зеленый"


def test_product_summ(
    samsung_1_product: "Smartphone", samsung_2_product: "Smartphone", lawngrass_1_product: "LawnGrass"
) -> None:
    """
    Проверяем сложение продуктов одинакового и разного классов
    """
    assert samsung_1_product + samsung_2_product == 2580000.0

    with pytest.raises(TypeError):
        samsung_1_product + lawngrass_1_product


def test_add_product_wrong_type(samsung_1_product: "Smartphone", samsung_2_product: "Smartphone") -> None:
    """
    Проверяем фильтр принадлежности к классу и подклассу в функции добавления продукта
    """
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [samsung_1_product, samsung_2_product]
    )
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")
