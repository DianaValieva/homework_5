import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope="session")
def open_browser():
    browser.driver.set_window_size(width=1920, height=1080)
    browser.config.timeout=2
    driver_options=webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options=driver_options
    yield browser
    browser.quit()

