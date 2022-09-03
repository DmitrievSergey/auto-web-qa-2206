from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage
from src.page_objects.admin_pages.CategoriesPage import CategoriesPage


class AdminPage(BasePage):
    CATALOG = (By.XPATH, "//a[contains(text(),'Catalog')]")
    CATEGORIES = (By.XPATH, "//a[contains(text(),'Categories')]")
    PRODUCTS = (By.XPATH, "//ul[@id='collapse1']//li//a[contains(text(),'Products')]")

    def click_catalog(self):
        self._click(self.CATALOG)
        return self

    def click_categories(self):
        self._verify_element_presence(self.CATEGORIES).click()
        return CategoriesPage(self.browser)

    def click_products(self):
        self._verify_element_presence(self.PRODUCTS).click()
        return self

    def verify_categories_presence(self):
        self._verify_element_presence(self.CATEGORIES)
        return self
