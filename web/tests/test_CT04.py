import time
import pytest
from web.pages.manager_page import ManagerPage

class Test_CT04:

    @pytest.mark.parametrize('all_browser', ['chrome'])
    def test_delete_customer_name(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.manager_Page()
        home_p.wait_home_buttons_be_visible()
        manager_p = ManagerPage(driver=home_p.driver)
        manager_p.wait_customer_list_button()
        manager_p.open_customer_list()
        manager_p.wait_customer_list()
        customer_name = manager_p.get_customer_name(customer_number=1)
        manager_p.delete_customer_data_in_list(customer_number=1)
        assert False == manager_p.customer_name_is_not_visible(customer_name.strip())


