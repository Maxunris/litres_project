from playwright.sync_api import Page, expect

class ProfilePage:
    def __init__(self, page: Page):
        self.page = page

    def open_profile(self):
        self.page.get_by_test_id("header__profile-button").click()

    def check_username(self, username):
        self.open_profile()
        expect(self.page.locator("#react-lc")).to_contain_text(username)

    def logout(self):
        self.open_profile()
        self.page.get_by_role("link", name="Выход").click()
