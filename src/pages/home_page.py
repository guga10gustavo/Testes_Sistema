from selenium.webdriver.common.by import By

class HomePage:
    customerBtn = '.center button[ng-click="customer()"]'
    managaerBtn = '.center button[ng-click="manager()"]'

    def __init__(self, browser):
        super(HomePage, self).__init__(driver=None, browser=browser)

    def manager_Page(self, open_browser):
        driver = open_browser
        driver.find_element(By.CSS_SELECTOR, self.managaerBtn).click()

    def customer_Page(self, open_browser):
        driver = open_browser
        driver.find_element(By.CSS_SELECTOR, self.customerBtn ).click()