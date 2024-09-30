import time

import pytest
from faker import Faker

from web.pages.manager_page import ManagerPage


class TestCT02:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_abrir_conta_e_verificar_na_lista(self, run_all_browser):
        fake = Faker()
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.manager_Page()
        add_customer_p = ManagerPage(driver=home_p.driver)
        add_customer_p.wait_manager_buttons_be_visible()
        add_customer_p.clicar_add_button()
        assert add_customer_p.validar_customer_aberto(), 'Add customer não foi aberto!'

        first_name = fake.first_name()
        last_name = fake.last_name()
        add_customer_p.preencher_campos(first_name, last_name)
        add_customer_p.save_customer()
        add_customer_p.clicar_open_account()
        add_customer_p.validar_open_account_aberto()
        add_customer_p.clicar_dropdown_customer()
        texto_encontrado = add_customer_p.validar_dropdown_customer_criado_text()
        assert first_name in texto_encontrado, "Cliente não aparece na lista de Customers"

        add_customer_p.clicar_option_customer()
        add_customer_p.clicar_dropdown_currency()
        add_customer_p.clicar_option_currency()
        add_customer_p.clicar_process_account()
        add_customer_p.pegar_account_number()
        texto_alert = add_customer_p.pegar_account_number()
        account_number = texto_alert[-4:]
        add_customer_p.fechar_popup()
        add_customer_p.acessar_lista_customers()
        add_customer_p.filtrar_novo_customer(account_number)
        assert add_customer_p.validar_item(), 'Item não encontrado'

