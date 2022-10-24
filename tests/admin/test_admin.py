import allure

from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage


@allure.title('Проверяем наличие элементов на экране авторизации в админку')
def test_admin_login_page_elements(browser):
    page = LoginAdminPage(browser)
    page.open_admin_page()
    page.verify_lock_icon_presence()
    page.verify_user_icon_presence()
    page.verify_input_username_presence()
    page.verify_input_password_presence()
    page.verify_submit_button_presence()
