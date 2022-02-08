from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.PageObject import PageObject

URL = 'https://www.saucedemo.com/'


class LoginPage(PageObject):
    id_login_btn = 'login-button'
    class_error_login = 'error-message-container'
    txt_username_required_error = 'Epic sadface: Username is required'

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.open_login_url()

    def open_login_url(self):
        self.driver.get(URL)

    def click_login_btn(self):
        self.driver.find_element(By.ID, self.id_login_btn).click()

    def is_url_login(self):
        return self.driver.current_url == URL

    def has_login_msg_error(self):
        error_message = self.driver.find_element(By.CLASS_NAME, self.class_error_login).text
        return error_message == self.txt_username_required_error

    def efetuar_login(self):
        # digitar username
        self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        # digitar password
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        # clicar no botão login
        self.click_login_btn()
