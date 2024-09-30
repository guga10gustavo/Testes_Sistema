# CT-002 -  Adicionar um cliente, abrir um conta e validar na lista de clientes
import pytest

from web.conftest import run_all_browser
from web.pages.manager_page import ManagerPage
from faker import Faker

class TestCT01:
    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_add_cliente_and_verify_client_list(self, run_all_browser):
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
        add_customer_p.acessar_lista_customers()
        add_customer_p.filtrar_novo_customer(first_name)
        assert add_customer_p.validar_item(), 'Item não encontrado'

