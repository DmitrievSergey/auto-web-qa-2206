import allure
import pytest

from src.page_objects.ItemPage import ItemPage


@allure.title('Проверяем наличие элементов на странице продукта')
@pytest.mark.parametrize('product_name, price, tax, points',
                         [("HP LP3065", "$122.00", "$100.00", "400")])
def test_item_page_elements(browser, product_name, price, tax, points):
    ItemPage(browser) \
        .open_item_page() \
        .verify_delivery_date_input_presence() \
        .verify_price_in_reward_points_presence(points) \
        .verify_product_name_presence(product_name) \
        .verify_product_price_presence(price) \
        .verify_product_tax_presence(tax)
