import time

import pytest

from web.pages.customer_page import CustomerPage

class TestTC08:

    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_access_client_deposit_and_reset_transactions(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.customer_Page()
        customer_p = CustomerPage(driver=home_p.driver)
        customer_p.wait_customer_account_btn()
        customer_p.customer_account()
        customer_p.wait_deposit_btn()
        customer_p.deposit()
        customer_p.wait_ammout_input()
        customer_p.deposit_or_withdrawl_amount(37009)
        customer_p.wait_success_message()
        customer_p.massageSucess()
        customer_p.transactions()
        customer_p.wait_reset_btn()
        customer_p.reset_transations()
        customer_p.click_back_btn()
        customer_p.wait_deposit_btn()
        customer_p.deposit()
        balance_value = customer_p.get_balance_value()

        assert int(balance_value.strip()) == 0

