from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class AdminPage(BasePage):
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    CATEGORIES = (By.XPATH, "//a[contains(text(),'Categories')]")
    PRODUCTS = (By.XPATH, "//ul[@id='collapse1']//li//a[contains(text(),'Products')]")

    def click_catalog(self):
        self._click(self.CATALOG)
        return self

    def click_categories(self):
        self._click(self.CATEGORIES)
        return self

    def click_products(self):
        self._click(self.PRODUCTS)
        # return self

    def verify_categories_presence(self):
        self._verify_element_presence(self.CATEGORIES)
        return self