from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage(BasePage):
    LOCATOR_WITH_PASSWORD = (By.ID, 'standard_auth_btn')
    LOCATOR_AUTH_EMAIL = (By.CSS_SELECTOR, "div#t-btn-tab-mail")
    LOCATOR_AUTH_LS = (By.ID, 't-btn-tab-ls')
    LOCATOR_AUTH_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_AUTH_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_EMAIL = (By.ID, 'username')
    LOCATOR_PASSWORD = (By.ID, 'password')
    LOCATOR_LS = (By.XPATH, '//*[@id=\"username\"]')
    LOCATOR_PHONE = (By.CSS_SELECTOR, 'input#username')
        # (By.XPATH, '//*[@id=\"username\"]')
    LOCATOR_LOGIN = (By.ID, 'kc-login')

    def click_on_with_password(self):
        return self.find_element(self.LOCATOR_WITH_PASSWORD).click()

    """Выбор авторизации по: почта, лицевой счет, телефон"""

    def click_auth_email(self):
        return self.find_element(self.LOCATOR_AUTH_EMAIL).click()

    def click_auth_ls(self):
        return self.find_element(self.LOCATOR_AUTH_LS).click()

    def click_auth_log(self):
        return self.find_element(self.LOCATOR_AUTH_LOGIN).click()

    def click_auth_phone(self):
        return self.find_element(self.LOCATOR_AUTH_PHONE).click()

    """Для полей ввода"""

    def get_input_email(self, email_value):
        return self.find_element(self.LOCATOR_EMAIL).send_keys(email_value)

    def get_input_password(self, password_value):
        return self.find_element(self.LOCATOR_PASSWORD).send_keys(password_value)

    def get_input_ls(self, ls_value):
        return self.find_element(self.LOCATOR_LS).send_keys(ls_value)

    def get_input_phone(self, phone_value):
        return self.find_element(self.LOCATOR_PHONE).send_keys(phone_value)

    def click_login(self):
        return self.find_element(self.LOCATOR_LOGIN).click()
