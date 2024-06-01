import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import allure
from litres_project.pages.login_page import LoginPage
from litres_project.pages.profile_page import ProfilePage

load_dotenv()
CORRECT_MAIL = os.getenv("CORRECT_MAIL")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")

@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login(page: Page, base_url):
    login_page = LoginPage(page)
    profile_page = ProfilePage(page)

    with allure.step('Open site and login'):
        login_page.open_login_page(base_url)
        login_page.enter_username(CORRECT_MAIL)
        login_page.enter_password(CORRECT_PASSWORD)
        login_page.close_phone_input_window()

    with allure.step('Check that the username is correct'):
        profile_page.check_username("maxtest2451")

    with allure.step('Checking the ability to log out of your account'):
        profile_page.logout()

@allure.title("invalid password")
@allure.tag('negative test')
def test_invalid_password(page: Page, base_url):
    login_page = LoginPage(page)

    with allure.step('Open site and enter invalid password'):
        login_page.open_login_page(base_url)
        login_page.enter_username(CORRECT_MAIL)
        login_page.enter_invalid_password(INCORRECT_PASSWORD)

    with allure.step('Check that the error message is correct'):
        expect(page.get_by_text("Неверное сочетание логина и пароля")).to_be_visible()

@allure.title("Empty login and password")
@allure.tag('negative test')
def test_empty_login_and_password(page: Page, base_url):
    login_page = LoginPage(page)

    with allure.step('Open site and submit empty username'):
        login_page.open_login_page(base_url)
        login_page.submit_empty_username()
        expect(page.get_by_test_id("authorization-popup").locator("form")).to_contain_text("Поле не может быть пустым")

    with allure.step('Enter username and submit empty password'):
        login_page.enter_username(CORRECT_MAIL)
        login_page.submit_empty_password()
        expect(page.get_by_test_id("authorization-popup").locator("form")).to_contain_text("Введите пароль")
