import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.recovery_page import RecoveryPage
from pages.register_page import RegisterPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def auth_page(browser):
    auth_page = AuthPage(browser)
    return auth_page

@pytest.fixture
def recovery_page(browser):
    recovery_page = RecoveryPage(browser)
    return recovery_page

@pytest.fixture
def register_page(browser):
    register_page= RegisterPage(browser)
    return register_page

