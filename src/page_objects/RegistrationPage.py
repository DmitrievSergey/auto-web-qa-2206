from selenium.webdriver.common.by import By

from .BasePage import BasePage


class RegistrationPage(BasePage):
    PATH = '/index.php?route=account/register'

    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[name='firstname']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[name='lastname']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    TELEPHONE_INPUT = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    PRIVACY_POLICY = (By.XPATH, "//input[@type='checkbox']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@type='submit']")

    REGISTER_ACCOUNT_TEXT = (By.XPATH, "//div[@id='account-register']//h1")
    YOUR_PERSONAL_DETAILS_TEXT = (By.XPATH, "//div[@id='account-register']//legend")
    SUCCESS_TITLE = (By.XPATH, "//div[@id='content']/h1")

    def open_registration_page(self):
        self._open_page(self.PATH)
        return self

    def get_success_title(self):
        title = self._verify_element_presence(self.SUCCESS_TITLE)
        return title.text

    def fill_telephone(self, value):
        self._input(self.TELEPHONE_INPUT, value)
        return self

    def fill_password(self, value):
        self._input(self.PASSWORD_INPUT, value)
        return self

    def fill_confirm(self, value):
        self._input(self.PASSWORD_CONFIRM, value)
        return self

    def click_privacy_policy(self):
        self._click(self.PRIVACY_POLICY)
        return self

    def click_continue(self):
        self._click(self.CONTINUE_BUTTON)
        return self

    def fill_firstname(self, value):
        self._input(self.FIRSTNAME_INPUT, value)
        return self

    def fill_lastname(self, value):
        self._input(self.LASTNAME_INPUT, value)
        return self

    def fill_email(self, value):
        self._input(self.EMAIL_INPUT, value)
        return self

    def verify_firstname_input_presence(self):
        self._verify_element_presence(self.FIRSTNAME_INPUT)
        return self

    def verify_lastname_input_presence(self):
        self._verify_element_presence(self.LASTNAME_INPUT)
        return self

    def verify_email_input_presence(self):
        self._verify_element_presence(self.EMAIL_INPUT)
        return self

    def verify_register_account_text_presence(self):
        self._verify_element_with_text_presence(self.REGISTER_ACCOUNT_TEXT, "Register Account")
        return self

    def verify_your_personal_details_text_presence(self):
        self._verify_element_with_text_presence(self.YOUR_PERSONAL_DETAILS_TEXT, "Your Personal Details")
        return self
