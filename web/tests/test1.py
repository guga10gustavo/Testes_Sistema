import time

import pytest


class Test1:

    @pytest.mark.parametrize('all_browser', ['chrome', 'edge'])
    def test_open(self, run_all_browser):
        home_p = run_all_browser
        home_p.wait_home_buttons_be_visible()
        home_p.manager_Page()
        time.sleep(2)
