from _pytest.capture import CaptureFixture

from src.classes import LawnGrass, Order, Product, Smartphone


def test_print_mixin(capsys: CaptureFixture) -> None:
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


def test_order_init(samsung_2_product: object) -> None:
    order = Order([samsung_2_product])
    assert order.products == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"


def test_order_total_pice(samsung_2_product: object) -> None:
    order = Order([samsung_2_product, samsung_2_product, samsung_2_product])
    assert order.total_price == 630000.0
