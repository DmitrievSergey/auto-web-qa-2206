import allure

from src.page_objects.admin_pages.AdminPage import AdminPage
from src.page_objects.admin_pages.CategoriesPage import CategoriesPage
from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage


@allure.title('Проверяем наличие элементов на странице категории в каталоге')
def test_admin_catalog_page_elements(browser):
    login_page = LoginAdminPage(browser)
    login_page.open_admin_page()
    login_page.login_in_admin(user_name='user', user_password='bitnami')

    admin_page = AdminPage(browser)
    admin_page.click_catalog()
    admin_page.click_categories()

    categories_page = CategoriesPage(browser)
    categories_page.verify_panel_title_presence()
    categories_page.verify_table_presence()
    categories_page.verify_categories_title_presence()
