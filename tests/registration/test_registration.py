from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(browser):
    browser.get(browser.url + "index.php?route=account/register")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@id='account-register']//h1"), "Register Account"))
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@id='account-register']//legend"), "Your Personal Details"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='firstname']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='lastname']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
