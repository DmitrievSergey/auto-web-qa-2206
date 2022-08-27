import pytest

from src.page_objects.MainPage import MainPage
from src.page_objects.elements.Elements import Elements


def test_search(browser):
    MainPage(browser) \
        .open_main_page() \
        .verify_cart_icon_presence() \
        .verify_my_account_presence() \
        .verify_share_icon_presence() \
        .verify_phone_icon_presence() \
        .verify_wish_icon_presence()


@pytest.mark.parametrize('currency',
                         ['EU', 'Pound', 'US'])
def test_currency_euro(browser, currency):
    MainPage(browser) \
        .open_main_page()
    Elements(browser) \
        .click_currency() \
        .choose_currency(currency)
    if currency == 'EU':
        assert Elements(browser).get_currency_icon() == '€'
    elif currency == 'Pound':
        assert Elements(browser).get_currency_icon() == '£'
    elif currency == 'US':
        assert Elements(browser).get_currency_icon() == '$'
