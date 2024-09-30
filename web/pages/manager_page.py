from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.pages.base import Base
import random

class ManagerPage(Base):

    customerBtn = 'button[ng-click="showCust()"]'
    searchCustomer = 'input[ng-model="searchCustomer"]'
    customersList = 'div table[class*="table"]'
    addCustomerBtn = (By.CSS_SELECTOR, ".center button[ng-class='btnClass1']")
    openAccountBtn = (By.CSS_SELECTOR, ".center button[ng-class='btnClass2']")
    firstNameField = (By.CSS_SELECTOR, "[ng-model = 'fName']")
    lastNameField = (By.CSS_SELECTOR, "[ng-model = 'lName']")
    postCodeField = (By.CSS_SELECTOR, "[ng-model = 'postCd'")
    saveCustomer = (By.CSS_SELECTOR, "[class = 'btn btn-default']")
    customers = (By.CSS_SELECTOR, ".center button[ng-click='showCust()']")
    searchCustomerTuple = (By.CSS_SELECTOR, ".input-group input[ng-model='searchCustomer']")
    tableItem = (By.CLASS_NAME, "ng-binding")
    customerDropdown = (By.ID, "userSelect")
    optionCustomer = (By.CSS_SELECTOR, "option[ng-repeat= 'cust in Customers']:last-of-type")
    currencyDropdown = (By.ID, "currency")
    optionCurrency = (By.CSS_SELECTOR, "#currency option:nth-of-type(2)")
    processBtn = (By.CSS_SELECTOR, "form button")

    fake = Faker()

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

    def escolhendo_post_code(self):
        post_code = random.randint(1, 1000)
        return post_code

    def escolhendo_currency(self):
        currency = random.randint(2, 4)
        print(f"currency: {currency}")
        return currency

    def wait_manager_buttons_be_visible(self):
        self.wait_element(self.addCustomerBtn)

    def clicar_add_button(self):
        self.driver.find_element(*self.addCustomerBtn).click()

    def validar_customer_aberto(self):
        aguardar_customer = self.wait_element(self.firstNameField)
        return aguardar_customer.is_displayed()

    def preencher_campos(self, first_name, last_name):
        self.driver.find_element(*self.firstNameField).send_keys(first_name)
        self.driver.find_element(*self.lastNameField).send_keys(last_name)
        self.driver.find_element(*self.postCodeField).send_keys(self.escolhendo_post_code())

    def save_customer(self):
        self.driver.find_element(*self.saveCustomer).click()
        self.desativar_pop_up()

    def acessar_lista_customers(self):
        self.driver.find_element(*self.customers).click()

    def filtrar_novo_customer(self, item):
        self.wait_element(self.searchCustomerTuple)
        self.driver.find_element(*self.searchCustomerTuple).send_keys(item)

    def validar_item(self):
        item_filtrado = self.wait_element(self.tableItem)
        return item_filtrado.is_displayed()

    def clicar_open_account(self):
        self.driver.find_element(*self.openAccountBtn).click()

    def validar_open_account_aberto(self):
        aguardar_customerDropdown = self.wait_element(self.customerDropdown)
        return aguardar_customerDropdown.is_displayed()

    def clicar_dropdown_customer(self):
        self.driver.find_element(*self.customerDropdown).click()

    def validar_dropdown_customer_criado(self):
        return self.driver.find_element(*self.optionCustomer)

    def validar_dropdown_customer_criado_text(self):
        return self.validar_dropdown_customer_criado().text

    def clicar_option_customer(self):
        self.driver.find_element(*self.optionCustomer).click()
        self.driver.find_element(By.TAG_NAME, 'body').click()

    def clicar_dropdown_currency(self):
        self.driver.find_element(*self.currencyDropdown).click()

    def clicar_option_currency(self):
        self.driver.find_element(*self.optionCurrency).click()
        self.driver.find_element(By.TAG_NAME, 'body').click()

    def clicar_process_account(self):
        self.driver.find_element(*self.processBtn).click()

    def pegar_account_number(self):
        try:
            WebDriverWait(self.driver, 100).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            texto_alert = alert.text
            # alert.accept()
            return texto_alert
        except:
            return None

    def fechar_popup(self):
        alert = self.driver.switch_to.alert
        alert.accept()