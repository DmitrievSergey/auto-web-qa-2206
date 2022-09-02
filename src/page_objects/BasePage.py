from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _open_page(self, page_url):
        self.browser.get(self.browser.url + page_url)

    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _verify_element_with_text_presence(self, locator: tuple, text):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    def _verify_alert_presence(self):
        try:
            return WebDriverWait(self.browser, self.browser.t).until(EC.alert_is_present())
        except TimeoutException:
            raise AssertionError("Cant find element alert")

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _input(self, locator: tuple, value):
        element = self._verify_element_presence(locator)
        element.click()
        element.clear()
        element.send_keys(value)
