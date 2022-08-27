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

    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, self.browser.t) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

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

    def _input(self, locator: tuple, value):
        element = self._verify_element_presence(locator)
        element.click()
        element.clear()
        element.send_keys(value)

    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _simple_click_element(self, element):
        element.click()

    def _click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    def _click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    def click_link(self, link_text):
        self._click((By.LINK_TEXT, link_text))
        return self

    def element_in_element(self, parent_locator: tuple, child_locator: tuple):
        return self.element(parent_locator).find_elements(*child_locator)

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")
