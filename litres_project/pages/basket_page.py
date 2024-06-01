from playwright.sync_api import Page, expect

class BasketPage:
    def __init__(self, page: Page):
        self.page = page

    def open_book_page(self, base_url, book_path):
        self.page.goto(f"{base_url}{book_path}")

    def check_book_title(self, title):
        expect(self.page.locator("h1")).to_contain_text(title)

    def add_book_to_cart(self):
        self.page.get_by_test_id("book__addToCartButton").click()

    def close_banner(self):
        self.page.get_by_test_id("modal__close--button").get_by_role("img").click()

    def go_to_cart(self):
        self.page.get_by_role("link", name="Корзина").click()
        expect(self.page.locator("h1")).to_contain_text("Корзина")

    def check_book_in_cart(self, book_title):
        expect(self.page.get_by_test_id("cart__bookCardTitle--wrapper").get_by_role("link")).to_contain_text(book_title)

    def delete_book_from_cart(self):
        self.page.get_by_test_id("cart__listDeleteButton").click()
        self.page.get_by_test_id("cart__modalDeleteArt").get_by_role("button", name="Удалить", exact=True).click()

    def check_cart_is_empty(self):
        expect(self.page.get_by_test_id("cart__emptyState--wrapper").get_by_role("heading")).to_contain_text("Корзина пуста")
