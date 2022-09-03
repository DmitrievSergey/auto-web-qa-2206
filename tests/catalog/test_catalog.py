from src.page_objects.admin_pages.AdminPage import AdminPage
from src.page_objects.admin_pages.CategoriesPage import CategoriesPage
from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage


def test_admin_catalog_page_elements(browser):
    LoginAdminPage(browser) \
        .open_admin_page() \
        .login_in_admin(user_name='user', user_password='bitnami')

    AdminPage(browser) \
        .click_catalog() \
        .click_categories()

    CategoriesPage(browser) \
        .verify_panel_title_presence() \
        .verify_table_presence() \
        .verify_categories_title_presence()


