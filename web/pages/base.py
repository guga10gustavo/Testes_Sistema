import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    cwd = os.getcwd()
    baseCwd = os.path.dirname(cwd)
    def __init__(self, driver, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                browser_path = self.baseCwd+'\\driver\\chromedriver.exe'
                s = Service(browser_path)
                self.driver = webdriver.Chrome(service=s)
            elif browser == 'edge':
                browser_path = self.baseCwd + '\\driver\\msedgedriver.exe'
                s = Service(browser_path)
                self.driver = webdriver.Edge(service=s)
            else:
                raise Exception('Browser não suportado!')

    # Substiuir __init__ para execução em MAC OS
    # def __init__(self, driver, browser=None):
    #     if driver:
    #         self.driver = driver
    #     else:
    #         if browser == 'chrome':
    #             self.driver = webdriver.Chrome()
    #         # elif browser == 'safari':
    #             #     self.driver = webdriver.Safari()
    #         elif browser == 'firefox':
    #             self.driver = webdriver.Firefox()
    #         else:
    #             raise Exception('Browser não suportado!')

    def is_url(self, url):
        return self.driver.current_url == url

    def wait_element(self, element_tuple, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(element_tuple))

    def desativar_pop_up(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()  # Ignora o alerta
        except:
            print("Nenhum alerta encontrado.")

    def close(self):
        self.driver.quit()