from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search(browser):
    browser.get(browser.url + "admin")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))).send_keys("user")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='password']"))).send_keys("bitnami")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Catalog')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Categories')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Categories')]")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@class ='panel-title']")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-bordered table-hover']")))
