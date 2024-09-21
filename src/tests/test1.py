import pytest


class Test1:

    @pytest.mark.parametrize('all_browser', ['chrome', 'safari', 'firefox'])

    def test_click_login_button(self, run_all_browser):
        login_p = run_all_browser
        login_p.click_login_button()

        assert login_p.is_url_login(), "URL inválida, mudou de página!"
        assert login_p.has_login_title(), 'Title inválido!'

        assert login_p.has_login_message_error(), 'Messagem de erro não encontrada!'