import os
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.login_page import LoginPage

load_dotenv()
CORRECT_MAIL = os.getenv("CORRECT_MAIL")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")

@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login(page: Page, base_url):
    login_page = LoginPage()

    login_page.set_page(page)
    login_page.set_base_url(base_url)

    login_page.open_login_page()
    login_page.enter_username(CORRECT_MAIL)
    login_page.enter_password(CORRECT_PASSWORD)
    login_page.close_phone_input_window()
    login_page.open_profile()
    login_page.check_username("maxtest2451")
    login_page.logout()

@allure.title("invalid password")
@allure.tag('negative test')
def test_invalid_password(page: Page, base_url):
    login_page = LoginPage()


    login_page.set_page(page)
    login_page.set_base_url(base_url)

    login_page.open_login_page()
    login_page.enter_username(CORRECT_MAIL)
    login_page.enter_invalid_password(INCORRECT_PASSWORD)
    login_page.check_invalid_password_error()

@allure.title("Empty login and password")
@allure.tag('negative test')
def test_empty_login_and_password(page: Page, base_url):
    login_page = LoginPage()

    login_page.set_page(page)
    login_page.set_base_url(base_url)

    login_page.open_login_page()
    login_page.submit_empty_username()
    login_page.check_empty_username_error()

    login_page.enter_username(CORRECT_MAIL)
    login_page.submit_empty_password()
    login_page.check_empty_password_error()
