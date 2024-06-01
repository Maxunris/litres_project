from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def open_login_page(self, base_url):
        self.page.goto(base_url)
        self.page.get_by_role("link", name="Войти").click()

    def enter_username(self, username):
        self.page.get_by_test_id("auth__input--enterEmailOrLogin").fill(username)
        self.page.get_by_test_id("auth__button--continue").click()
        self.page.get_by_text("Пароль", exact=True).click()

    def enter_password(self, password):
        self.page.get_by_test_id("auth__input--enterPassword").fill(password)
        self.page.get_by_test_id("auth__button--enter").click()

    def enter_invalid_password(self, password):
        self.page.get_by_test_id("auth__input--enterPassword").fill(password)
        self.page.get_by_test_id("auth__button--enter").click()

    def submit_empty_username(self):
        self.page.get_by_test_id("auth__button--continue").click()

    def submit_empty_password(self):
        self.page.get_by_test_id("auth__button--enter").click()

    def close_phone_input_window(self):
        self.page.get_by_test_id("phone-input").click()
        self.page.get_by_role("button", name="Позже").click()
