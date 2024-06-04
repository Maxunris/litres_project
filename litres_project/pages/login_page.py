from playwright.sync_api import Page, expect
import allure
from litres_project.pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Open login page')
    def open_login_page(self):
        self.page.goto(self.base_url)
        self.page.get_by_role("link", name="Войти").click()

    @allure.step('Enter username')
    def enter_username(self, username):
        self.page.get_by_test_id("auth__input--enterEmailOrLogin").fill(username)
        self.page.get_by_test_id("auth__button--continue").click()
        self.page.get_by_text("Пароль", exact=True).click()

    @allure.step('Enter password')
    def enter_password(self, password):
        self.page.get_by_test_id("auth__input--enterPassword").fill(password)
        self.page.get_by_test_id("auth__button--enter").click()

    @allure.step('Enter invalid password')
    def enter_invalid_password(self, password):
        self.page.get_by_test_id("auth__input--enterPassword").fill(password)
        self.page.get_by_test_id("auth__button--enter").click()

    @allure.step('Submit empty username')
    def submit_empty_username(self):
        self.page.get_by_test_id("auth__button--continue").click()

    @allure.step('Submit empty password')
    def submit_empty_password(self):
        self.page.get_by_test_id("auth__button--enter").click()

    @allure.step('Close phone input window')
    def close_phone_input_window(self):
        self.page.get_by_test_id("phone-input").click()
        self.page.get_by_role("button", name="Позже").click()

    @allure.step('Check error message for invalid password')
    def check_invalid_password_error(self):
        expect(self.page.get_by_text("Неверное сочетание логина и пароля")).to_be_visible()

    @allure.step('Check empty username error')
    def check_empty_username_error(self):
        expect(self.page.get_by_test_id("authorization-popup").locator("form")).to_contain_text("Поле не может быть пустым")

    @allure.step('Check empty password error')
    def check_empty_password_error(self):
        expect(self.page.get_by_test_id("authorization-popup").locator("form")).to_contain_text("Введите пароль")

    @allure.step('Open profile page')
    def open_profile(self):
        self.page.get_by_test_id("header__profile-button").click()

    @allure.step('Check that the username is correct')
    def check_username(self, username):
        expect(self.page.locator("#react-lc")).to_contain_text(username)

    @allure.step('Log out')
    def logout(self):
        self.page.get_by_role("link", name="Выход").click()

