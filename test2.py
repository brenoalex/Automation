import pytest

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


class Test2:
    @pytest.fixture()
    def test_setup(self):
        self.login_page = LoginPage(browser='chrome')
        yield
        self.login_page.close()

    def test_efetuar_login(self, test_setup):
        self.login_page.efetuar_login()

        assert not self.login_page.is_url_login(), \
            'Página de Produtos não encontrada!'

        self.products_page = ProductsPage(self.login_page.driver)
        assert self.products_page.is_products_page(), \
            'Página de Produtos não encontrada!'