from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class Elements(BasePage):
    CURRENCY = (By.XPATH, "//span[contains(text(),'Currency')]")
    EURO = (By.XPATH, "//button[contains(text(),'€ Euro')]")
    POUND = (By.XPATH, "//button[contains(text(),'£ Pound Sterling')]")
    US = (By.XPATH, "//button[contains(text(),'$ US Dollar')]")
    CURRENCY_ICON = (By.XPATH, "//form[@id='form-currency']/div/button/strong")

    def get_currency_icon(self):
        element = self._verify_element_presence(self.CURRENCY_ICON)
        return element.text

    def click_currency(self):
        self._verify_element_presence(self.CURRENCY).click()
        return self

    def choose_currency(self, currency):
        if currency == 'EU':
            self._verify_element_presence(self.EURO).click()
        elif currency == 'US':
            self._verify_element_presence(self.US).click()
        elif currency == 'Pound':
            self._verify_element_presence(self.POUND).click()
        return self