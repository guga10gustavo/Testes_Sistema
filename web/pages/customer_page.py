from select import select

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from web.pages.base import Base


class CustomerPage(Base):
    selectCustomerBtn = 'userSelect'
    custumerAccount = '#userSelect > option:nth-child(2)'
    loginBtn = 'body > div > div > div.ng-scope > div > form > button'
    transactionsBtn = 'button[ng-click="transactions()"]'
    depositBtn = 'button[ng-click="deposit()"]'
    withdrawlBtn = 'button[ng-click="withdrawl()"]'
    amountInput = 'input[placeholder="amount"]'
    amountBtn = 'button[type="submit"]'
    massageShow = 'span[ng-show="message"]'
    accountInput = 'accountSelect'
    selectAccount = '#accountSelect option:nth-child(1)'
    balanceValue = 'div[ng-hide="noAccount"] strong:nth-child(2)'
    resetTransations = 'button[ng-click="reset()"]'
    backbtn='button[ng-click="back()"]'
    withdrawlform = 'form[ng-submit="withdrawl()"]'
    your_name_select = (By.ID, "userSelect")
    optionCustomer = (By.CSS_SELECTOR, "option[class= 'ng-binding ng-scope']:last-of-type")
    loginBtnTuple = (By.CSS_SELECTOR, "*[class = 'btn btn-default']")
    account_number_select = (By.ID, "accountSelect")
    account_number_option = (By.CSS_SELECTOR, "#accountSelect option:last-of-type")
    account_number_text = (By.CSS_SELECTOR, "strong[class='ng-binding']:first-of-type")
    def __init__(self, driver):
        super(CustomerPage, self).__init__(driver=driver)

    def wait_customer_account_btn(self):
        self.wait_element((By.ID, self.selectCustomerBtn))
    def customer_account(self):
        select = self.driver
        select.find_element(By.ID, self.selectCustomerBtn).click()
        select.find_element(By.CSS_SELECTOR, self.custumerAccount).click()
        select.find_element(By.CSS_SELECTOR, self.loginBtn).click()

    def transactions(self):
        select = self.driver
        select.find_element(By.CSS_SELECTOR, self.transactionsBtn).click()

    def click_back_btn(self):
        self.driver.find_element(By.CSS_SELECTOR,self.backbtn).click()
    def wait_reset_btn(self):
        self.wait_element((By.CSS_SELECTOR,self.resetTransations))

    def reset_transations(self):
        self.driver.find_element(By.CSS_SELECTOR,self.resetTransations).click()

    def wait_deposit_btn(self):
        self.wait_element((By.CSS_SELECTOR, self.depositBtn))
    def deposit(self):
        select = self.driver
        select.find_element(By.CSS_SELECTOR, self.depositBtn).click()

    def withdrawl(self):
        select = self.driver
        select.find_element(By.CSS_SELECTOR, self.withdrawlBtn).click()

    def wait_ammout_input(self):
        self.wait_element((By.CSS_SELECTOR, self. amountInput))

    def wait_withdrawl_form(self):
        self.wait_element((By.CSS_SELECTOR, self.withdrawlform))

    def deposit_or_withdrawl_amount(self, value):
        select = self.driver
        select.find_element(By.CSS_SELECTOR, self. amountInput).click()
        select.find_element(By.CSS_SELECTOR, self. amountInput).send_keys(value)
        select.find_element(By.CSS_SELECTOR, self.amountBtn).click()

    def massageSucess(self):
        select = self.driver
        select.find_element(By.CSS_SELECTOR, self.massageShow)

    def wait_success_message(self):
        self.wait_element((By.CSS_SELECTOR, self.massageShow))

    def wait_select_account(self):
        self.wait_element((By.ID, self.accountInput))

    def select_account(self):
        select = self.driver
        select.find_element(By.ID, self.accountInput).click()
        select.find_element(By.CSS_SELECTOR, self.selectAccount).click()
        select.find_element(By.ID, self.accountInput).click()
        return select.find_element(By.CSS_SELECTOR, self.selectAccount).text

    def get_balance_value(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.balanceValue).text

    def check_account_number(self,account_number):
        return self.driver.find_element(By.XPATH, '//div[@ng-hide="noAccount"]//strong[normalize-space(text())="'+account_number.__str__()+'"]').is_displayed()

    def clicar_select_your_name(self):
        self.wait_element(self.your_name_select)
        self.driver.find_element(*self.your_name_select).click()

    def validar_dropdown_your_name(self):
        return self.driver.find_element(*self.optionCustomer)

    def clicar_customer(self):
        self.driver.find_element(*self.optionCustomer).click()
        self.driver.find_element(By.TAG_NAME, 'body').click()

    def validar_botao_login(self):
        return self.driver.find_element(*self.loginBtnTuple)

    def clicar_login(self):
        self.driver.find_element(*self.loginBtnTuple).click()

    def clicar_select_account_number(self):
        self.wait_element(self.account_number_select)
        self.driver.find_element(*self.account_number_select).click()

    def escolher_option_account_number(self):
        account_number = self.driver.find_element(*self.account_number_option).text
        self.driver.find_element(*self.account_number_option).click()
        self.driver.find_element(By.TAG_NAME, 'body').click()
        return account_number

    def validar_account_number_tela(self):
        account_number = self.driver.find_element(*self.account_number_text).text
        return account_number