import datetime
import logging
import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self._logger_config()

    def _logger_config(self):
        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    @allure.step("Открываем url {page_url}")
    def _open_page(self, page_url):
        self.logger.info(
            "Opening url: {} at {} in test {}".format(page_url, datetime.datetime.now(), self.browser.test_name))
        self.browser.get(self.browser.url + page_url)

    @allure.step("Ждем пока появится элемент {locator}")
    def _verify_element_presence(self, locator: tuple):
        try:
            self.logger.info("Check if element {} is present at {}".format(locator, datetime.datetime.now()))
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screen_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Ждем пока появится текст {text} локатор {locator}")
    def _verify_element_with_text_presence(self, locator: tuple, text):
        try:
            self.logger.info("Check if text {} is present at ".format(text, datetime.datetime.now()))
            return WebDriverWait(self.browser, self.browser.t).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screen_image",
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError("Cant find element by locator: {}".format(locator))

    @allure.step("Ждем alert")
    def _verify_alert_presence(self):
        try:
            self.logger.info("Check if alert is present at {}".format(datetime.datetime.now()))
            return WebDriverWait(self.browser, self.browser.t).until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError("Cant find element alert")

    @allure.step("Кликаем на элемент {locator}")
    def _click(self, locator: tuple):
        self.logger.info("Clicking element: {} at {}".format(locator, datetime.datetime.now()))
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _element(self, locator: tuple):
        try:
            self.logger.info("Check if element {} is present at {}".format(locator, datetime.datetime.now()))
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    @allure.step("Заполняем input {locator} значением {value}")
    def _input(self, locator: tuple, value):
        self.logger.info("Fill in element {} with text {} at {}".format(locator, value, datetime.datetime.now()))
        element = self._verify_element_presence(locator)
        element.click()
        element.clear()
        element.send_keys(value)
