from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ItemPage(BasePage):
    PATH = '/laptop-notebook/hp-lp3065'

    PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='col-sm-4']>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='col-sm-4']>ul>li>h2")
    PRODUCT_TAX = (By.XPATH, "//div/ul/li[contains(text(),'Ex Tax:')]")
    PRICE_IN_REWARD_POINTS = (By.XPATH, "//div/ul/li[contains(text(),'Price in reward points:')]")
    DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, "div[class='input-group date']>input[type='text']")

    def open_item_page(self):
        self._open_page(self.PATH)
        return self

    def verify_product_name_presence(self):
        self._verify_element_with_text_presence(self.PRODUCT_NAME, "HP LP3065")
        return self

    def verify_product_price_presence(self):
        self._verify_element_with_text_presence(self.PRODUCT_PRICE, "$122.00")
        return self

    def verify_product_tax_presence(self):
        self._verify_element_with_text_presence(self.PRODUCT_TAX, "$100.00")
        return self

    def verify_price_in_reward_points_presence(self):
        self._verify_element_with_text_presence(self.PRICE_IN_REWARD_POINTS, "400")
        return self

    def verify_delivery_date_input_presence(self):
        self._verify_element_presence(self.DELIVERY_DATE_INPUT)
        return self


