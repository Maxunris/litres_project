from playwright.sync_api import Page

class BasePage():

    def __init__(self, page: Page = None):
        self.page = page
        self.base_url = None

    def set_page(self, page: Page):
        self.page = page

    def set_base_url(self, base_url):
        self.base_url = base_url
