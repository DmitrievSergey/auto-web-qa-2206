from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[class='fa fa-phone']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='My Account']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[class='fa fa-heart']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[class='fa fa-shopping-cart']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[class='fa fa-share']")))
