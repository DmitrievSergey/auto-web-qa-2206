from src.page_objects.admin_pages.LoginAdminPage import LoginAdminPage


def test_search(browser):
    LoginAdminPage(browser) \
        .open_admin_page() \
        .verify_lock_icon_presence() \
        .verify_user_icon_presence() \
        .verify_input_username_presence() \
        .verify_input_password_presence() \
        .verify_submit_button_presence()
