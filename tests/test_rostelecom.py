from pages.auth_page import AuthPage
from pages.register_page import RegisterPage
from pages.recovery_page import RecoveryPage

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from selenium.common.exceptions import TimeoutException

"""№1 Авторизация по связке почта+пароль, позитивный тест"""
@pytest.mark.xfail(reason="Тест падает из-за капчи")
def test_authorization_valid_email(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_email()
    auth_page.get_input_email('вставить валидные тестовые данные')
    auth_page.get_input_password('вставить валидные тестовые данные')
    wait = WebDriverWait(browser, 5)
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.ID, 'button-1023')
        )
        assert True
    except TimeoutException:
        assert False
#
"""№2 Авторизация по связке лицевой счет+пароль, позитивный тест"""

def test_authorization_valid_ls(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_ls()
    auth_page.get_input_ls('вставить валидные тестовые данные')
    auth_page.get_input_password('вставить валидные тестовые данные')
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"drop-down-1031\"]/div/div/svg'))
        )
        assert True
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        browser.save_screenshot('result_2_auth_val_ls.png')
        assert False

"""№3 Авторизация по связке почта+пароль, негативный тест"""
#
def test_authorization_invalid_email_pass(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_email()
    auth_page.get_input_email('mcvfrmail.ru')
    auth_page.get_input_password('1234')
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"form-error-message\"]'))
        )
        browser.save_screenshot('result_3_auth_inval_email_pass.png')
        assert True
    except TimeoutException:
        assert False

"""№4 Авторизация по связке лцевой счет+пароль, негативный тест"""
def test_authorization_invalid_ls_pass(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_ls()
    auth_page.get_input_ls(22222)
    auth_page.get_input_password('1234')
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"username-meta\"]'))
            )
        browser.save_screenshot('result_4_auth_inval_ls_pass.png')
        assert True
    except TimeoutException:
        assert False

"""№5 Авторизация по номеру телефона, негативный тест"""
def test_authorization_invalid_phone_pass(browser, auth_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    # browser.refresh()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_phone()
    auth_page.get_input_phone(999999999)
    auth_page.get_input_password('Mdvn')
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"username-meta\"]'))
        )
        browser.save_screenshot('result_5_auth_inval_ph_pass.png')
        assert True
    except Exception as e:
        print(f"Вход с невалидными данными - ошибка: {e}")
        assert False

"""Вспомогательные функции для генерации тетсовых данных"""
def generate_string(n):
    return "x" * n

def englisch_chars():
    return 'abcdefghijklmnopqrstuvwyz'

def russ_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:.[]{}'

"""№6 Валидация поля "Почта", негативный тест"""
@pytest.mark.parametrize('email_value',
                         [generate_string(255),  special_chars(), englisch_chars(), russ_chars(), 'М', 123],
                         ids=['255 symbols', 'specials', 'englisch', 'russian',  '1 symbol', 'digit'])
def test_field_email_auth(browser, auth_page, email_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_email()
    auth_page.get_input_email(email_value)
    auth_page.get_input_password('вставить валидные тестовые данные')
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"form-error-message\"]'))
        )
        assert True
    except TimeoutException:
        assert False

"""№7 Валидация поля пароль, негативный тест"""
@pytest.mark.parametrize('password_value',
                         [generate_string(21), generate_string(7), special_chars(), englisch_chars(), russ_chars(), 'A', 1234567],
                         ids=['21 symbols', '7 symbols', 'specials', 'englisch', 'russian',  '1 symbol', 'digit'])
def test_field_password_auth(browser, auth_page, password_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_email()
    auth_page.get_input_email('вставитьвалидные тестовые данные')
    auth_page.get_input_password(password_value)
    auth_page.click_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"form-error-message\"]'))
        )
        assert True
    except TimeoutException:
        assert False

"""№8 Валидация поля Лицевой счет, негативный тест"""
@pytest.mark.xfail(reason="Идет сброс на логин и появляется капча")
@pytest.mark.parametrize('ls_value',
                         [12345678912, 1234567891012, 1],
                         ids=['digit-11', 'digit-13', 'digit-1'])
def test_field_ls_auth(browser,auth_page, ls_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_ls()
    auth_page.get_input_ls(ls_value)
    auth_page.get_input_password('вставитьвалидные тестовые данные')
    auth_page.click_auth_login()
    if WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"username-meta\"]'))
        ):
        assert True
    else:
        assert False

"""№9 Валидация поля Телефон, негативный тест"""
@pytest.mark.xfail(reason="Идет сброс на логин и появляется капча")
@pytest.mark.parametrize('phone_value',
                         [1234567891, 123456789, 1],
                         ids=['digit-10', 'digit-9', 'digit-1'])
def test_field_phone_auth(browser,auth_page, phone_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_phone()
    auth_page.get_input_phone(phone_value)
    auth_page.get_input_password('вставить валидные тестовые данные')
    auth_page.click_auth_login()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"username-meta\"]'))
        )
        assert True
    except TimeoutException:
        assert False

"""№10 Активность кнопки Забыли пароль по связке почта+пароль"""
def test_forgot_password_email(browser, auth_page, recovery_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_email()
    recovery_page.click_forgot_pass()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"card-title\"]'))
        )
        assert True
    except TimeoutException:
        assert False

"""№11 Активность кнопки Забыли пароль по связке лицевой счет+пароль"""
def test_forgot_password_ls(browser, auth_page, recovery_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_ls()
    auth_page.get_input_ls(278011897889)
    recovery_page.click_forgot_pass()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"card-title\"]'))
        )
        assert True
    except TimeoutException:
        assert False

"""№12 Активность кнопки Забыли пароль по связке логин+пароль"""
def test_forgot_password_login(browser, auth_page, recovery_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_log()
    recovery_page.click_forgot_pass()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id=\"card-title\"]'))
        )
        assert True
    except TimeoutException:
        assert False

"""№13 Активность кнопки "Забыли пароль" по связке телефон+пароль"""
def test_forgot_password_phone(browser, auth_page, recovery_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    auth_page.click_auth_phone()
    recovery_page.click_forgot_pass()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/section[2]/div/div[1]/h1'))
        )
        assert True
    except TimeoutException:
        assert False

"""№14 Активность кнопки "Зарегистрироваться" """
@pytest.mark.xfail(reason="Появляется капча и тест падает")
def test_activity_register(browser, auth_page, register_page):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    register_page.click_btn_register()
    if WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/p[1]')
        ):
        assert True
    else:
        assert False
#
"""№15 Регистрация: валидация поля "Имя" """
@pytest.mark.parametrize('name_value',
                         [generate_string(31),  special_chars(), englisch_chars(), 'A', 12345],
                         ids=['31 symbols', 'specials', 'englisch', '1 symbol', 'digit'])
def test_field_name_register(browser, auth_page, register_page, name_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    register_page.click_btn_register()
    register_page.get_input_name(name_value)
    register_page.get_input_surname('Иванов')
    register_page.get_input_region('Санкт-Петербург г')
    register_page.LOCATOR_EMAIL_OR_PHONE('Iv@mail.ru')
    register_page.get_input_pass('12345mmM')
    register_page.get_input_pass_2('12345mmM')
    register_page.click_btn_reg_account()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[1]/div[1]/span')
        )
        assert True
    except TimeoutException:
        assert False

"""№16 Регистрация: валидация поля "Фамилия" """
@pytest.mark.parametrize('surname_value',
                         [generate_string(31),  special_chars(), englisch_chars(),  'A', 12345],
                         ids=['31 symbols', 'specials', 'englisch', '1 symbol', 'digit'])
def test_field_surname_register(browser, auth_page, register_page, surname_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    register_page.click_btn_register()
    register_page.get_input_name('Иван')
    register_page.get_input_surname(surname_value)
    register_page.get_input_region('Санкт-Петербург г')
    register_page.LOCATOR_EMAIL_OR_PHONE('Iv@mail.ru')
    register_page.get_input_pass('12345mmM')
    register_page.get_input_pass_2('12345mmM')
    register_page.click_btn_reg_account()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[1]/div[2]/span')
        )
        assert True
    except TimeoutException:
        assert False

"""№17 Регистрация: валидация поля "Регион" """
def test_field_region_register(browser, auth_page, register_page, region_value=''):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 10)
    register_page.click_btn_register()
    register_page.get_input_region(region_value)
    register_page.click_btn_reg_account()
    try:
        WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(By.XPATH, '//*[@id=\"page-right\"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/span[1]')
        )
        assert True
    except Exception as e:
        print(f"Ошибка: {e}")
        assert False

"""№18 Валидация поля "E-mail или мобильный телефон" на странице регистрация по почте"""
@pytest.mark.parametrize('email_value',
                         [generate_string(255), special_chars(), englisch_chars(), russ_chars(), 'A', 12345],
                         ids=['255 symbols', 'specials', 'englisch', 'russian',  '1 symbol', 'digit'])
def test_field_email_register(browser, auth_page, register_page, email_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    register_page.click_btn_register()
    register_page.get_input_name('Иван')
    register_page.get_input_surname('Иванов')
    register_page.get_input_region('Санкт-Петербург г')
    register_page.LOCATOR_EMAIL_OR_PHONE(email_value)
    register_page.get_input_pass('12345mmM')
    register_page.get_input_pass_2('12345mmM')
    register_page.click_btn_reg_account()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/form/div[1]/div[2]/span')
        )
        assert True
    except TimeoutException:
        assert False

"""№19 Валидация поля "Пароль" на странице регистрация"""
@pytest.mark.parametrize('pass_value',
                         [generate_string(21), generate_string(7), russ_chars(), special_chars(), englisch_chars(),  'A', 12345],
                         ids=['21 symbols', '7 symbols', 'russian', 'specials', 'englisch', '1 symbol', 'digit'])
def test_field_name_register(browser, auth_page, register_page, pass_value):
    auth_page.go_to_site()
    auth_page.click_on_with_password()
    wait = WebDriverWait(browser, 5)
    register_page.click_btn_register()
    register_page.get_input_name('Иван')
    register_page.get_input_surname('Иванов')
    register_page.get_input_region('Санкт-Петербург г')
    register_page.LOCATOR_EMAIL_OR_PHONE('Iv@mail..ru')
    register_page.get_input_pass(pass_value)
    register_page.click_btn_reg_account()
    current_url = browser.current_url
    expected_url = \
        "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=lk_b2c&tab_id=N-mWNSLA0NY"
    if current_url == expected_url:
        assert True
    else:
        assert False

"""№20 Проверка активной гиперссылки Помощь"""
def test_btn_help(browser, auth_page, recovery_page):
    auth_page.go_to_site()
    wait = WebDriverWait(browser, 10)
    recovery_page.click_on_help()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.XPATH, '//*[@id=\"page-right\"]/div/div[1]/div/div/div/p')
        )
        assert True
    except TimeoutException:
        assert False

