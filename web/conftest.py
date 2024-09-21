import pytest

from web.pages.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser to run tests.')


@pytest.fixture
def run_all_browser(all_browser):
    home_p = HomePage(browser=all_browser)
    home_p.open_app()
    yield home_p
    home_p.close()


@pytest.fixture
def open_browser(request):
    selected_browser = request.config.getoption('browser_selenium').lower()
    home_p = HomePage(browser=selected_browser)
    home_p.open_app()
    yield home_p
    home_p.close()


@pytest.fixture
def navegate_to_home(open_browser):
    home_p = open_browser
    yield home_p
