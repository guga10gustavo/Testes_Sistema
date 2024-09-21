from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from web.pages.base import Base


class ManagerPage(Base):

    customerBtn = 'button[ng-click="showCust()"]'
    searchCustomer = 'input[ng-model="searchCustomer"]'
    customersList = 'div table[class*="table"]'
    def __init__(self, driver):
        super(ManagerPage, self).__init__(driver=driver)
    def open_customer_list(self):
        self.driver.find_element(By.CSS_SELECTOR, self.customerBtn).click()

    def wait_customer_list_button(self):
        self.wait_element((By.CSS_SELECTOR, self.customerBtn))
    def wait_customer_list(self):
        self.wait_element((By.CSS_SELECTOR, self.customersList))

    def get_customer_name(self, customer_number):
        custumer_name = self.driver.find_element(By.CSS_SELECTOR, 'div table[class*="table"] tbody tr:nth-child('+customer_number.__str__()+') td:nth-child(1)').text
        return custumer_name

    def type_customer_name(self,customer_name):
        self.driver.find_element(By.CSS_SELECTOR,self.searchCustomer).send_keys(customer_name)

    def get_search_customers_result(self):
        customers_name_array = self.driver.find_elements(By.CSS_SELECTOR, 'div table[class*="table"] tbody tr td:nth-child(1)')
        return customers_name_array

    def delete_customer_data_in_list(self,customer_number):
        self.driver.find_element(By.CSS_SELECTOR, 'div table[class*="table"] tbody tr:nth-child('+customer_number.__str__()+') td:nth-child(5) button').click()

    def customer_name_is_not_visible(self,customer_name):
        try:
            self.driver.find_element(By.XPATH, '//tbody//tr//td[normalize-space(text())="'+customer_name+'"]').is_displayed()
            return True
        except NoSuchElementException:
            return False

    def click_first_name_sort(self):
        self.driver.find_element(By.CSS_SELECTOR, 'thead td:nth-child(1) a[ng-click*="sortType"]').click()