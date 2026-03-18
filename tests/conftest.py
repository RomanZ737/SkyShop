import pytest

from src.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def product_1() -> Product:
    """
    Фикстура возвращает данные для проверки инициализации класса Product
    """
    return Product("Samsung Galaxy S23 Ultra",
                   "256GB, Серый цвет, 200MP камера",
                   180000.0, 5)


@pytest.fixture
def product4() -> Product:
    return Product("55\" QLED 4K",
                   "Фоновая подсветка",
                   123000.0, 7)


@pytest.fixture
def category1() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    return category1


@pytest.fixture
def data_for_json_file_open() -> str:
    """
    Фукстура возвращает выходные данные
    для json_file_open
    """
    return """{"id": 441945886}"""


@pytest.fixture
def wrong_data_for_json_file_open() -> str:
    """
    Фукстура возвращает выходные данные
    для json_file_open
    """
    return """"""


@pytest.fixture
def output_new_init_class_test() -> str:
    return r"""Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
55" QLED 4K, 123000.0 руб. Остаток: 7 шт.
"""


@pytest.fixture
def new_product_test_input_data() -> dict:
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
            "quantity": 5}


@pytest.fixture
def samsung_1_product() -> Smartphone:
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0,
                      5, 95.5,"S23 Ultra", 256, "Серый")


@pytest.fixture
def samsung_2_product() -> Smartphone:
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                      98.2, "15", 512, "Gray space")


@pytest.fixture
def lawngrass_1_product() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20,
                     "Россия", "7 дней", "Зеленый")

@pytest.fixture
def lawngrass_2_product() -> LawnGrass:
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15,
                     "США", "5 дней", "Темно-зеленый")