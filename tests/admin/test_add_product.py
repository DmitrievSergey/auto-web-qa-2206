import allure
import pytest

from src.page_objects.admin_pages.AdminPage import AdminPage
from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage
from src.page_objects.admin_pages.ProductsPage import ProductsPage


@allure.title('Проверяем добавление продукта')
@pytest.mark.parametrize('product_name, meta_name, model',
                         [('product4', 'meta4', 'model4')])
def test_add_new_product(browser, product_name, meta_name, model):
    login_page = LoginAdminPage(browser)
    login_page.open_admin_page()
    login_page.login_in_admin(user_name='user', user_password='bitnami')

    admin_page = AdminPage(browser)
    admin_page.click_catalog()
    admin_page.click_products()

    product_page = ProductsPage(browser)
    product_page.click_add_product_button()
    product_page.add_new_product(product_name, meta_name, model)
    assert product_page.get_list_of_name_and_model(product_name, model) == [(product_name, model)]
