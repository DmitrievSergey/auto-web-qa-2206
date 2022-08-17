from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(browser):
    browser.get(browser.url + "laptop-notebook/hp-lp3065")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='col-sm-4']>h1"), "HP LP3065"))
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='col-sm-4']>ul>li>h2"), "$122.00"))
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div/ul/li[contains(text(),'Ex Tax:')]"), "$100.00"))
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, "//div/ul/li[contains(text(),'Price in reward points:')]"), "400"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='input-group date']>input[type='text']")))
