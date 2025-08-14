from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage(BasePage):
    LOCATOR_BTN_REGISTER = (By.XPATH, '//*[@id=\"kc-register\"]')
    LOCATOR_NAME = (By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    LOCATOR_SURNAME = (By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    LOCATOR_REGION = (By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[2]/div/div/input')
    LOCATOR_EMAIL_OR_PHONE = (By.XPATH, '//*[@id=\"address\"]')
    LOCATOR_REG_PASSWORD = (By.XPATH, '//*[@id=\"password\"]')
    LOCATOR_REG_PASSWORD_2 = (By.XPATH, '//*[@id=\"password-confirm\"]')
    LOCATOR_REG_ACCOUNT = (By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/button[1]')

    def click_btn_register(self):
        return self.find_element(self.LOCATOR_BTN_REGISTER).click()

    def get_input_name(self, name_value):
        return self.find_element(self.LOCATOR_NAME).send_keys(name_value)

    def get_input_surname(self, surname_value):
        return self.find_element(self.LOCATOR_SURNAME).send_keys(surname_value)

    def get_input_region(self, region_value):
        return self.find_element(self.LOCATOR_REGION).send_keys(region_value)

    def get_input_email_or_phone(self, email_value):
        return self.find_element(self.LOCATOR_EMAIL_OR_PHONE).send_keys(email_value)

    def get_input_pass(self, pass_value):
        return self.find_element(self.LOCATOR_REG_PASSWORD).send_keys(pass_value)

    def get_input_pass_2(self, pass_value):
        return self.find_element(self.LOCATOR_REG_PASSWORD_2).send_keys(pass_value)

    def click_btn_reg_account(self):
        return self.find_element(self.LOCATOR_REG_ACCOUNT).submit()
