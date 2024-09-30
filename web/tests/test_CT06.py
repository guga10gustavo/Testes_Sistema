import time

import pytest

from web.pages.customer_page import CustomerPage

class TestTC06:

    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_access_client_deposit_and_validate(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.customer_Page()
        customer_p = CustomerPage(driver=home_p.driver)
        customer_p.wait_customer_account_btn()
        customer_p.customer_account()
        customer_p.wait_deposit_btn()
        customer_p.transactions()
        customer_p.deposit()
        customer_p.wait_ammout_input()
        balance_original_value = customer_p.get_balance_value()
        customer_p.deposit_or_withdrawl_amount(37009)
        customer_p.wait_success_message()
        customer_p.massageSucess()
        balance_current_value = customer_p.get_balance_value()
        balance_subtotal= int(balance_original_value.strip()) + 37009
        assert balance_subtotal == int(balance_current_value.strip())