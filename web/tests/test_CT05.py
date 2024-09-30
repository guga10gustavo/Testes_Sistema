import time

import pytest
from faker import Faker

from web.pages.customer_page import CustomerPage
from web.pages.manager_page import ManagerPage

class TestCT05:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_abrir_conta_verficar_troca_entre_contas(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.manager_Page()

        home_p.home_Page()
        home_p.wait_home_buttons_be_visible()
        home_p.customer_Page()
        login_customer_p = CustomerPage(driver=home_p.driver)
        login_customer_p.clicar_select_your_name()

        login_customer_p.clicar_customer()
        assert login_customer_p.validar_botao_login(), 'Botão de Login não aparece!'
        login_customer_p.clicar_login()
        login_customer_p.clicar_select_account_number()
        login_customer_p.escolher_option_account_number()
        assert login_customer_p.escolher_option_account_number() == login_customer_p.validar_account_number_tela(), \
            f"Os valores não são iguais: {login_customer_p.escolher_option_account_number()} != {login_customer_p.validar_account_number_tela()}"
