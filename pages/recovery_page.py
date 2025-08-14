from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RecoveryPage(BasePage):
    LOCATOR_FORGOT_PASS = (By.XPATH, '//*[@id=\"forgot_password\"]')
    LOCATOR_HELP = (By.XPATH, '//*[@id=\"faq-open\"]/a')

    """Забыли пароль"""

    def click_forgot_pass(self):
        return self.find_element(self.LOCATOR_FORGOT_PASS).click()

    """Помощь"""
    def click_on_help(self):
        return self.find_element(self.LOCATOR_HELP).click()
