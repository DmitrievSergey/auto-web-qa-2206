from src.page_objects.MainPage import MainPage


def test_main_page_element(browser):
    MainPage(browser) \
        .open_main_page() \
        .verify_cart_icon_presence() \
        .verify_my_account_presence() \
        .verify_share_icon_presence() \
        .verify_phone_icon_presence() \
        .verify_wish_icon_presence()
