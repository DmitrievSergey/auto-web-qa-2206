import pytest

from src.page_classes.Product import Product
from src.page_objects.admin_pages.AdminPage import AdminPage
from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage
from src.page_objects.admin_pages.ProductsPage import ProductsPage


def test_search(browser):
    LoginAdminPage(browser) \
        .open_admin_page() \
        .login_in_admin()
    AdminPage(browser) \
        .click_catalog() \
        .click_categories() \
        .verify_panel_title_presence() \
        .verify_table_presence() \
        .verify_categories_title_presence()


@pytest.mark.parametrize('product_name, meta_name, model',
                         [('product4', 'meta4', 'model4')])
def test_add_new_product(browser, product_name, meta_name, model):
    LoginAdminPage(browser) \
        .open_admin_page() \
        .login_in_admin()
    AdminPage(browser) \
        .click_catalog() \
        .click_products()
    ProductsPage(browser) \
        .click_add_product_button() \
        .add_new_product(product_name, meta_name, model)
    assert ProductsPage(browser).get_list_of_name_and_model(product_name, model) == [(product_name, model)]


@pytest.mark.parametrize('product_name, model',
                         [('product4', 'model4')])
def test_delete_product(browser, product_name, model):
    LoginAdminPage(browser) \
        .open_admin_page() \
        .login_in_admin()
    AdminPage(browser) \
        .click_catalog() \
        .click_products()
    ProductsPage(browser) \
        .delete_product(product_name, model)
    assert ProductsPage(browser).get_count_of_product(product_name, model) == 1
    assert ProductsPage(browser).find_no_result().text == "No results!"
