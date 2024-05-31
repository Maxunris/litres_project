import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import allure

load_dotenv()
CORRECT_MAIL = os.getenv("CORRECT_MAIL")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")


@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login(page: Page, base_url):
    with allure.step('Open site'):
        page.goto(base_url)

    with allure.step('The login button is clickable'):
        page.get_by_role("link", name="Войти").click()

    with allure.step('Enter username'):
        page.get_by_test_id("auth__input--enterEmailOrLogin").fill(CORRECT_MAIL)
        page.get_by_test_id("auth__input--enterEmailOrLogin").click()
        page.get_by_test_id("auth__button--continue").click()
        page.get_by_text("Пароль", exact=True).click()

    with allure.step('Enter  password'):
        page.get_by_test_id("auth__input--enterPassword").fill(CORRECT_PASSWORD)
        page.get_by_test_id("auth__button--enter").click()

    with allure.step('Closing the phone input window'):
        page.get_by_test_id("phone-input").click()
        page.get_by_role("button", name="Позже").click()

    with allure.step('Сheck that the username is correct'):
        page.get_by_test_id("header__profile-button").click()
        expect(page.locator("#react-lc")).to_contain_text("maxtest2451")

    with allure.step('Checking the ability to log out of your account'):
        page.get_by_test_id("header__profile-button").click()
        page.get_by_role("link", name="Выход").click()


@allure.title("invalid password")
@allure.tag('negative test')
def test_invalid_password(page: Page, base_url):
    with allure.step('Open site'):
        page.goto(base_url)

    with allure.step('The login button is clickable'):
        page.get_by_role("link", name="Войти").click()

    with allure.step('Enter your username'):
        page.get_by_test_id("auth__input--enterEmailOrLogin").fill(CORRECT_MAIL)
        page.get_by_test_id("auth__input--enterEmailOrLogin").click()
        page.get_by_test_id("auth__button--continue").click()
        page.get_by_text("Пароль", exact=True).click()

    with allure.step('Enter invalid password'):
        page.get_by_test_id("auth__input--enterPassword").fill(INCORRECT_PASSWORD)
        page.get_by_test_id("auth__button--enter").click()

    with allure.step('Check that the error message is correct'):
        expect(page.get_by_text("Неверное сочетание логина и пароля")).to_be_visible()


@allure.title("Empty login and password")
@allure.tag('negative test')
def test_empty_login_and_password(page: Page, base_url):
    with allure.step('Open site'):
        page.goto(base_url)

    with allure.step('The login button is clickable'):
        page.get_by_role("link", name="Войти").click()

    with allure.step('Enter empty username'):
        page.get_by_test_id("auth__button--continue").click()
        expect(page.get_by_test_id("authorization-popup").locator("form")).to_contain_text("Поле не может быть пустым")

    with allure.step('Enter your username'):
        page.get_by_test_id("auth__input--enterEmailOrLogin").fill(CORRECT_MAIL)
        page.get_by_test_id("auth__input--enterEmailOrLogin").click()
        page.get_by_test_id("auth__button--continue").click()
        page.get_by_text("Пароль", exact=True).click()

    with allure.step('Enter empty password'):
        page.get_by_test_id("auth__button--enter").click()
        expect(page.get_by_test_id("authorization-popup").locator("form")).to_contain_text("Введите пароль")
