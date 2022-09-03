from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class CategoriesPage(BasePage):
    CATEGORIES_TITLE = (By.XPATH, "//h1[contains(text(), 'Categories')]")
    PANEL_TITLE = (By.XPATH, "//h3[@class ='panel-title']")
    TABLE = (By.XPATH, "//table[@class='table table-bordered table-hover']")

    def verify_categories_title_presence(self):
        self._verify_element_presence(self.CATEGORIES_TITLE)
        return self

    def verify_panel_title_presence(self):
        self._verify_element_presence(self.PANEL_TITLE)
        return self

    def verify_table_presence(self):
        self._verify_element_presence(self.TABLE)
        return self

