from playwright.sync_api import Page, expect
import allure

class FavoritesPage:
    def __init__(self, page: Page = None):
        self.page = page
        self.base_url = None

    def set_page(self, page: Page):
        self.page = page

    def set_base_url(self, base_url):
        self.base_url = base_url

    @allure.step('Open search')
    def open_search_page(self, query):
        self.page.goto(f"search/?q={query}")

    @allure.step('Adding a book to favorites')
    def add_book_to_favorites(self):
        self.page.locator(".LikeButton_likeButton__hix0G").first.click()

    @allure.step('Go to favorites')
    def go_to_favorites(self):
        self.page.get_by_role("link", name="icon-favorite 1 Отложенные").click()

    @allure.step('Checking the number of books')
    def check_number_of_books(self, count):
        expect(self.page.get_by_test_id("navigation__tabsList")).to_contain_text(f"Отложено{count}")

    @allure.step('Check the title of the book and the author')
    def check_book_details(self, title, author):
        expect(self.page.get_by_test_id("art__title").get_by_role("paragraph")).to_contain_text(title)
        expect(self.page.get_by_test_id("art__authorName")).to_contain_text(author)

    @allure.step('Deleting a book from favorites')
    def remove_book_from_favorites(self):
        self.page.get_by_test_id("art__wrapper").get_by_test_id("popover__baseElement").locator("a").click()
        self.page.get_by_text("Убрать из отложенного").click()

    @allure.step('Check that there are no books in the favorites')
    def check_no_books_in_favorites(self):
        expect(self.page.get_by_test_id("navigation__tabsList")).to_contain_text("Отложено")
