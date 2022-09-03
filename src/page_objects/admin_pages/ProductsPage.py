from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class ProductsPage(BasePage):
    ADD_PRODUCT_BUTTON = (By.XPATH, "//div[@class='pull-right']//a[@class='btn btn-primary']")
    DELETE_BUTTON = (By.XPATH, "//button[@class='btn btn-danger']")

    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    DATA_TAB = (By.XPATH, "//a[contains(text(),'Data')]")

    PRODUCT_NAME_INPUT = (By.XPATH, "//input[@id='input-name1']")
    META_TAG_TITLE_INPUT = (By.XPATH, "//input[@id='input-meta-title1']")
    MODEL_INPUT = (By.XPATH, "//input[@id='input-model']")

    PAGES_LIST = (By.XPATH, "//ul[@class='pagination']/li")

    FILTER_PRODUCT_NAME_INPUT = (By.XPATH, "//input[@id='input-name']")
    FILTER_MODEL_INPUT = (By.XPATH, "//input[@id='input-model']")
    FILTER_BUTTON = (By.XPATH, "//button[@id='button-filter']")

    LIST_OF_PRODUCTS = (By.XPATH, "//tbody/tr")
    ELEMENT_LIST_OF_PRODUCT = (By.XPATH, "./td")

    NO_RESULTS = (By.XPATH, "//tbody/tr/td[@class='text-center']")

    def click_save_button(self):
        self.logger.info("Нажали кнопку Сохранить")
        self._click(self.SAVE_BUTTON)

    def click_data_tab(self):
        self._click(self.DATA_TAB)
        return self

    def add_new_product(self, product_name, meta_name, model):
        self.logger.info("Зашли в метод add_new_product ")
        self._input(self.PRODUCT_NAME_INPUT, product_name)
        self._input(self.META_TAG_TITLE_INPUT, meta_name)
        self.click_data_tab()
        self._input(self.MODEL_INPUT, model)
        self.click_save_button()
        self.logger.info("Завершили добавление продукта")

    def click_add_product_button(self):
        self._click(self.ADD_PRODUCT_BUTTON)
        return self

    def find_product_by_filter(self, product_name, model):
        self._input(self.FILTER_PRODUCT_NAME_INPUT, product_name)
        self._input(self.FILTER_MODEL_INPUT, model)
        self._click(self.FILTER_BUTTON)

    def find_no_result(self):
        return self._verify_element_presence(self.NO_RESULTS)

    def accept_alert(self):
        self._verify_alert_presence().accept()

    def get_count_of_product(self, product, model):
        self.find_product_by_filter(product, model)
        return len(self.browser.find_elements(*self.LIST_OF_PRODUCTS))

    def get_list_of_name_and_model(self, product, model):
        self.logger.info("Зашли в метод get_list_of_name_and_model")
        list_of_name_and_model = []
        self.find_product_by_filter(product, model)
        product_list = self.browser.find_elements(*self.LIST_OF_PRODUCTS)
        count = len(product_list)
        while count > 0:
            name = product_list[count - 1].find_elements(*self.ELEMENT_LIST_OF_PRODUCT)[2].text
            model = product_list[count - 1].find_elements(*self.ELEMENT_LIST_OF_PRODUCT)[3].text
            list_of_name_and_model.append((name, model))
            count -= 1
            print(list_of_name_and_model)
        return list_of_name_and_model

    def delete_product(self, product, model):
        self.find_product_by_filter(product, model)
        product_list = self.browser.find_elements(*self.LIST_OF_PRODUCTS)
        if self.find_no_result().text == "No results!":
            self.click_add_product_button()
            self.add_new_product(product, 'meta', model)
        count = len(product_list)
        while count > 0:
            product_list = self.browser.find_elements(*self.LIST_OF_PRODUCTS)
            product_list[count - 1].find_elements(*self.ELEMENT_LIST_OF_PRODUCT)[0].click()
            self._verify_element_presence(self.DELETE_BUTTON).click()
            self.accept_alert()
            count -= 1
        return self
