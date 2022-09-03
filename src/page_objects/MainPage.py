from selenium.webdriver.common.by import By

from .BasePage import BasePage


class MainPage(BasePage):
    PATH = '/'
    PHONE_ICON = (By.CSS_SELECTOR, "i[class='fa fa-phone']")
    WISH_ICON = (By.CSS_SELECTOR, "i[class='fa fa-heart']")
    CART_ICON = (By.CSS_SELECTOR, "i[class='fa fa-shopping-cart']")
    SHARE_ICON = (By.CSS_SELECTOR, "i[class='fa fa-share']")
    MY_ACCOUNT = (By.CSS_SELECTOR, "a[title='My Account']")

    def open_main_page(self):
        return self._open_page(self.PATH)

    def verify_phone_icon_presence(self):
        self._verify_element_presence(self.PHONE_ICON)
        return self

    def verify_wish_icon_presence(self):
        self._verify_element_presence(self.WISH_ICON)
        return self

    def verify_cart_icon_presence(self):
        self._verify_element_presence(self.CART_ICON)
        return self

    def verify_share_icon_presence(self):
        self._verify_element_presence(self.SHARE_ICON)
        return self

    def verify_my_account_presence(self):
        self._verify_element_presence(self.MY_ACCOUNT)
        return self
