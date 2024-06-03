from playwright.sync_api import Page, expect
import allure

class BasketPage:
    def __init__(self, page: Page = None):
        self.page = page
        self.base_url = None

    def set_page(self, page: Page):
        self.page = page

    def set_base_url(self, base_url):
        self.base_url = base_url

    @allure.step('Open book')
    def open_book_page(self, book_path):
        self.page.goto(f"{self.base_url}{book_path}")

    @allure.step('Checking the title of the book')
    def check_book_title(self, title):
        expect(self.page.locator("h1")).to_contain_text(title)

    @allure.step('Adding a book to the basket')
    def add_book_to_cart(self):
        self.page.get_by_test_id("book__addToCartButton").click()

    @allure.step('Closing the banner')
    def close_banner(self):
        self.page.get_by_test_id("modal__close--button").get_by_role("img").click()

    @allure.step('Go to the basket')
    def go_to_cart(self):
        self.page.get_by_role("link", name="Корзина").click()
        expect(self.page.locator("h1")).to_contain_text("Корзина")

    @allure.step('Check that the necessary book is in the basket')
    def check_book_in_cart(self, book_title):
        expect(self.page.get_by_test_id("cart__bookCardTitle--wrapper").get_by_role("link")).to_contain_text(book_title)

    @allure.step('Deleting a book from the basket')
    def delete_book_from_cart(self):
        self.page.get_by_test_id("cart__listDeleteButton").click()
        self.page.get_by_test_id("cart__modalDeleteArt").get_by_role("button", name="Удалить", exact=True).click()

    @allure.step('Check that the basket is empty')
    def check_cart_is_empty(self):
        expect(self.page.get_by_test_id("cart__emptyState--wrapper").get_by_role("heading")).to_contain_text("Корзина пуста")
