from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from web.pages.base import Base


class HomePage(Base):
    customerBtn = '.center button[ng-click="customer()"]'
    managerBtn = '.center button[ng-click="manager()"]'
    base_Url = 'https://globalsqa.com/angularJs-protractor/BankingProject/#/login'
    home_btns = (By.CSS_SELECTOR, managerBtn)
    homeBtn = (By.CSS_SELECTOR, '*[class = "btn home"]')

    def __init__(self, browser):
        super(HomePage, self).__init__(driver=None, browser=browser)
    def open_app(self):
        self.driver.get(self.base_Url)

    def manager_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.managerBtn).click()

    def customer_Page(self):
        self.driver.find_element(By.CSS_SELECTOR, self.customerBtn).click()

    def wait_home_buttons_be_visible(self):
        self.wait_element(self.home_btns)

    def home_Page(self):
        self.driver.find_element(*self.homeBtn).click()
