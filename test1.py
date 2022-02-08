import pytest

from pages.LoginPage import LoginPage

URL = 'https://www.saucedemo.com/'


class Test1:
    @pytest.fixture()
    def test_setup(self):
        self.login_page = LoginPage(browser='firefox')
        yield
        self.login_page.close()

    def test_click_login_btn(self, test_setup):
        self.login_page.click_login_btn()
        assert self.login_page.is_url_login(), 'Página requerida não permaneceu a mesma!'
        assert self.login_page.has_login_msg_error(), 'Mensagem de erro não encontrada!'


