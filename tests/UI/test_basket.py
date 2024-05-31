import os
import time

from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import allure

load_dotenv()
CORRECT_MAIL = os.getenv("CORRECT_MAIL")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")


@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login(page: Page, base_url):
    with allure.step('Open book'):
        page.goto(base_url + "aleksandr-duma/graf-monte-kristo-5957159/")

    with allure.step('Checking the title of the book'):
        expect(page.locator("h1")).to_contain_text("Граф Монте-Кристо")

    with allure.step('Adding a book to the basket'):
        page.get_by_test_id("book__addToCartButton").click()

    with allure.step('Closing the banner'):
        page.get_by_test_id("modal__close--button").get_by_role("img").click()

    with allure.step('Go to the basket'):
        page.get_by_role("link", name="Корзина").click()
        expect(page.locator("h1")).to_contain_text("Корзина")

    with allure.step('Check that the necessary book is in the basket'):
        expect(page.get_by_test_id("cart__bookCardTitle--wrapper").get_by_role("link")).to_contain_text(
            "Граф Монте-Кристо")

    with allure.step('Deleting a book from the basket'):
        page.get_by_test_id("cart__listDeleteButton").click()
        page.get_by_test_id("cart__modalDeleteArt").get_by_role("button", name="Удалить", exact=True).click()

    with allure.step('Check that the basket is empty'):
        expect(page.get_by_test_id("cart__emptyState--wrapper").get_by_role("heading")).to_contain_text(
            "Корзина пуста")

