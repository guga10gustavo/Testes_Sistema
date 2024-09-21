import time
import pytest
from web.pages.manager_page import ManagerPage

class Test_CT03:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_search_customer_name(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.manager_Page()
        home_p.wait_home_buttons_be_visible()
        manager_p = ManagerPage(driver=home_p.driver)
        manager_p.wait_customer_list_button()
        manager_p.open_customer_list()
        manager_p.wait_customer_list()
        customer_name = manager_p.get_customer_name(customer_number=1)
        manager_p.type_customer_name(customer_name=customer_name)
        custumers_name = manager_p.get_search_customers_result()
        for name in custumers_name:
            assert (name.text).strip() == customer_name.strip()


