import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--tolerance", type=int, default=3)


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    tolerance = request.config.getoption("--tolerance")

    if browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()
    driver.maximize_window()

    # request.addfinalizer(driver.close)
    driver.url = url
    driver.t = tolerance

    return driver
