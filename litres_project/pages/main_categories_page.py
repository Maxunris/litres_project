from playwright.sync_api import Page, expect
import allure

class NavigationPage:
    def __init__(self, page: Page = None):
        self.page = page
        self.base_url = None

    def set_page(self, page: Page):
        self.page = page

    def set_base_url(self, base_url):
        self.base_url = base_url

    @allure.step('Open popular page')
    def open_popular_page(self):
        if not self.base_url:
            raise ValueError("Base URL is not set")
        self.page.goto(f"{self.base_url}popular/")

    @allure.step('Navigate to subscription page')
    def go_to_subscription_page(self):
        self.page.goto("https://www.litres.ru/litres_subscription/")
        self.page.get_by_role("link", name="Подписка за 0 ₽").click()
        expect(self.page.get_by_test_id("subscription-landing-content")).to_contain_text("Попробовать бесплатно")

    @allure.step('Navigate to promo code page')
    def go_to_promo_code_page(self):
        self.page.get_by_role("link", name="Промокод").click()
        expect(self.page.locator("#putmoney")).to_contain_text("Активация промокода Литрес")

    @allure.step('Navigate to new books page')
    def go_to_new_books_page(self):
        self.page.get_by_role("link", name="Новинки").click()
        expect(self.page.get_by_role("heading")).to_contain_text("Новинки книг")

    @allure.step('Navigate to popular books page')
    def go_to_popular_books_page(self):
        self.page.get_by_role("link", name="Популярное").click()
        expect(self.page.get_by_role("heading")).to_contain_text("Лучшие книги")

    @allure.step('Navigate to collections page')
    def go_to_collections_page(self):
        self.page.get_by_role("link", name="Подборки").click()
        expect(self.page.locator("h1")).to_contain_text("Подборки")

    @allure.step('Navigate to audiobooks page')
    def go_to_audiobooks_page(self):
        self.page.get_by_role("link", name="Аудиокниги").click()
        expect(self.page.locator("h1")).to_contain_text("Аудиокниги")

    @allure.step('Navigate to exclusives page')
    def go_to_exclusives_page(self):
        self.page.get_by_role("link", name="Эксклюзивы").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Эксклюзивы Литрес")

    @allure.step('Navigate to drafts page')
    def go_to_drafts_page(self):
        self.page.get_by_role("link", name="Черновики").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Черновики")

    @allure.step('Navigate to podcasts page')
    def go_to_podcasts_page(self):
        self.page.get_by_role("link", name="Подкасты").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Подкасты")

    @allure.step('Navigate to comics page')
    def go_to_comics_page(self):
        self.page.get_by_role("link", name="Комиксы").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Комиксы")

    @allure.step('Navigate to journal page')
    def go_to_journal_page(self):
        self.page.get_by_role("link", name="Журнал").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Литрес: Журнал")
