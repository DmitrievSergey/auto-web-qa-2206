import allure
import pytest

from src.page_objects.admin_pages.AdminPage import AdminPage
from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage
from src.page_objects.admin_pages.ProductsPage import ProductsPage


@allure.title('Проверяем удаление продукта')
@pytest.mark.parametrize('product_name, model',
                         [('product4', 'model4')])
def test_delete_product(browser, product_name, model):
    login_admin_page = LoginAdminPage(browser)
    login_admin_page.open_admin_page()
    login_admin_page.login_in_admin(user_name='user', user_password='bitnami')

    admin_page = AdminPage(browser)
    admin_page.click_catalog()
    admin_page.click_products()

    product_page = ProductsPage(browser)
    product_page.delete_product(product_name, model)
    assert product_page.get_count_of_product(product_name, model) == 1
    assert product_page.find_no_result().text == "No results!"
