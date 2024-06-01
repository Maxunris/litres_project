from playwright.sync_api import Page, expect

class FavoritesPage:
    def __init__(self, page: Page):
        self.page = page

    def open_search_page(self, base_url, query):
        self.page.goto(f"{base_url}search/?q={query}")

    def add_book_to_favorites(self):
        self.page.locator(".LikeButton_likeButton__hix0G").first.click()

    def go_to_favorites(self):
        self.page.get_by_role("link", name="icon-favorite 1 Отложенные").click()

    def check_number_of_books(self, count):
        expect(self.page.get_by_test_id("navigation__tabsList")).to_contain_text(f"Отложено{count}")

    def check_book_details(self, title, author):
        expect(self.page.get_by_test_id("art__title").get_by_role("paragraph")).to_contain_text(title)
        expect(self.page.get_by_test_id("art__authorName")).to_contain_text(author)

    def remove_book_from_favorites(self):
        self.page.get_by_test_id("art__wrapper").get_by_test_id("popover__baseElement").locator("a").click()
        self.page.get_by_text("Убрать из отложенного").click()

    def check_no_books_in_favorites(self):
        expect(self.page.get_by_test_id("navigation__tabsList")).to_contain_text("Отложено")
