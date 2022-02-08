from selenium import webdriver


class PageObject:

    def __init__(self, browser='chrome', driver=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

    def close(self):
        self.driver.quit()