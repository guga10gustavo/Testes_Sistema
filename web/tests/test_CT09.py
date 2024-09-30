import pytest
from web.pages.manager_page import ManagerPage

class Test_CT09:

    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_first_name_order_list(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.manager_Page()
        home_p.wait_home_buttons_be_visible()
        manager_p = ManagerPage(driver=home_p.driver)
        manager_p.wait_customer_list_button()
        manager_p.open_customer_list()
        manager_p.wait_customer_list()
        customer_names_elements = manager_p.get_search_customers_result()
        customer_names = []
        customer_names_sorted_inverse = []
        customer_names_sorted_ordered = []
        for name in customer_names_elements:
            customer_names.append(name.text.strip())
        manager_p.click_first_name_sort()
        customer_names_sorted_inverse_elements = manager_p.get_search_customers_result()
        for name in customer_names_sorted_inverse_elements:
            customer_names_sorted_inverse.append(name.text.strip())
        manager_p.click_first_name_sort()
        customer_names_sorted_ordered_elements = manager_p.get_search_customers_result()
        for name in customer_names_sorted_ordered_elements:
            customer_names_sorted_ordered.append(name.text.strip())
        customer_names.sort(reverse=True)
        assert customer_names == customer_names_sorted_inverse
        customer_names.sort()
        assert customer_names == customer_names_sorted_ordered




