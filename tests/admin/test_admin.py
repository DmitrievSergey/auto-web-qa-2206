from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(browser):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1>i[class='fa fa-lock']")))
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "label[for='input-username']"),
                                         "Username"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i[class='fa fa-user']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
