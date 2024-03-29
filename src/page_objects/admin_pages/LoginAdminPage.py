from selenium.webdriver.common.by import By

from src.page_objects.BasePage import BasePage


class LoginAdminPage(BasePage):
    PATH = '/admin'
    LOCK_ICON = (By.CSS_SELECTOR, "h1>i[class='fa fa-lock']")
    USER_ICON = (By.CSS_SELECTOR, "i[class='fa fa-user']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open_admin_page(self):
        self._open_page(self.PATH)

    def verify_lock_icon_presence(self):
        self._verify_element_presence(self.LOCK_ICON)

    def verify_user_icon_presence(self):
        self._verify_element_presence(self.USER_ICON)

    def verify_input_username_presence(self):
        self._verify_element_presence(self.USERNAME_INPUT)

    def verify_input_password_presence(self):
        self._verify_element_presence(self.PASSWORD_INPUT)

    def verify_submit_button_presence(self):
        self._verify_element_presence(self.SUBMIT_BUTTON)

    def login_in_admin(self, user_name, user_password):
        self._input(self.USERNAME_INPUT, user_name)
        self._input(self.PASSWORD_INPUT, user_password)
        self._click(self.SUBMIT_BUTTON)
