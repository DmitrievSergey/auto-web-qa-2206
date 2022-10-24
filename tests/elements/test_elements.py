import allure
import pytest

from src.page_objects.MainPage import MainPage
from src.page_objects.elements.Elements import Elements


@allure.title('Проверяем переключение валют')
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
