from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.home_page import HomePage

url_demo = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'

@pytest.fixture
def open_browser():
    driver = webdriver.Chrome()
    driver.get(url_demo)
    yield driver
    driver.quit()

@pytest.fixture
def run_all_browser(all_browser):
    home_p = HomePage(browser=all_browser)
    yield home_p
    home_p.close()

@pytest.fixture
def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help='Select browser to run tests.')





