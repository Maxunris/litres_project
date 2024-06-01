from playwright.sync_api import Page, expect

class NavigationPage:
    def __init__(self, page: Page):
        self.page = page

    def open_popular_page(self, base_url):
        self.page.goto(f"{base_url}popular/")

    def go_to_subscription_page(self):
        self.page.goto("https://www.litres.ru/litres_subscription/")
        self.page.get_by_role("link", name="Подписка за 0 ₽").click()
        expect(self.page.get_by_test_id("subscription-landing-content")).to_contain_text("Попробовать бесплатно")

    def go_to_promo_code_page(self):
        self.page.get_by_role("link", name="Промокод").click()
        expect(self.page.locator("#putmoney")).to_contain_text("Активация промокода Литрес")

    def go_to_new_books_page(self):
        self.page.get_by_role("link", name="Новинки").click()
        expect(self.page.get_by_role("heading")).to_contain_text("Новинки книг")

    def go_to_popular_books_page(self):
        self.page.get_by_role("link", name="Популярное").click()
        expect(self.page.get_by_role("heading")).to_contain_text("Лучшие книги")

    def go_to_collections_page(self):
        self.page.get_by_role("link", name="Подборки").click()
        expect(self.page.locator("h1")).to_contain_text("Подборки")

    def go_to_audiobooks_page(self):
        self.page.get_by_role("link", name="Аудиокниги").click()
        expect(self.page.locator("h1")).to_contain_text("Аудиокниги")

    def go_to_exclusives_page(self):
        self.page.get_by_role("link", name="Эксклюзивы").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Эксклюзивы Литрес")

    def go_to_drafts_page(self):
        self.page.get_by_role("link", name="Черновики").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Черновики")

    def go_to_podcasts_page(self):
        self.page.get_by_role("link", name="Подкасты").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Подкасты")

    def go_to_comics_page(self):
        self.page.get_by_role("link", name="Комиксы").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Комиксы")

    def go_to_journal_page(self):
        self.page.get_by_role("link", name="Журнал").click()
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text("Литрес: Журнал")
