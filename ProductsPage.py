from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

URL = 'https://www.saucedemo.com/inventory.html'


class ProductsPage(PageObject):
    txt_products_title = 'PRODUCTS'

    def __init__(self, driver):
        super(ProductsPage, self).__init__(driver=driver)

    def is_products_page(self):
        is_url_products = self.driver.current_url == URL
        has_products_title = self.driver.find_element(By.CLASS_NAME, 'title').text == self.txt_products_title
        try:
            self.driver.find_element(By.CLASS_NAME, 'inventory_item_price')
            return is_url_products and has_products_title
        except NoSuchElementException:
            return False

