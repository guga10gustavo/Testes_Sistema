from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, browser):
        super(HomePage, self).__init__(driver=None, browser=browser)

    def home_botton(self, open_browser):
        driver = open_browser
        driver.find_element(By.CLASS_NAME, 'btn home').click()