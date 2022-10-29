import datetime
import logging

import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://demo.opencart.com")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--tolerance", type=int, default=5)
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="local")
    parser.addoption("--bversion", action="store", default="106.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=False)


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    tolerance = request.config.getoption("--tolerance")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    version = request.config.getoption("--bversion")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    executor_url = f"http://{executor}:4444/wd/hub"

    if executor != "local":
        capabilities = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": video,
                "enableLog": logs
            },
            "name": "name"
        }
        driver = webdriver.Remote(
            desired_capabilities=capabilities,
            command_executor=executor_url
        )

    elif browser == "chrome":
        service = ChromiumService(executable_path=drivers + "/chromedriver106")
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")
    else:
        driver = webdriver.Safari()
    driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    driver.get(url)
    driver.url = url
    driver.t = tolerance

    logger.info("Browser:{}, Session {}".format(browser, driver.session_id, driver.capabilities))

    def clear_loggers():
        """Remove handlers from all loggers"""
        loggers = [logging.getLogger()] + list(logging.Logger.manager.loggerDict.values())
        for log in loggers:
            if not hasattr(log, "handlers"):
                continue
            for handler in log.handlers[:]:
                log.removeHandler(handler)

    def fin():
        driver.quit()
        logger.info("driver.quit {}, at {}".format(driver.session_id, datetime.datetime.now()))
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))
        clear_loggers()

    request.addfinalizer(fin)

    return driver
