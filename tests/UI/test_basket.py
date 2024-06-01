import os
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.basket_page import BasketPage

load_dotenv()

@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login(page: Page, base_url):
    basket_page = BasketPage(page)

    with allure.step('Open book'):
        basket_page.open_book_page(base_url, "aleksandr-duma/graf-monte-kristo-5957159/")

    with allure.step('Checking the title of the book'):
        basket_page.check_book_title("Граф Монте-Кристо")

    with allure.step('Adding a book to the basket'):
        basket_page.add_book_to_cart()

    with allure.step('Closing the banner'):
        basket_page.close_banner()

    with allure.step('Go to the basket'):
        basket_page.go_to_cart()

    with allure.step('Check that the necessary book is in the basket'):
        basket_page.check_book_in_cart("Граф Монте-Кристо")

    with allure.step('Deleting a book from the basket'):
        basket_page.delete_book_from_cart()

    with allure.step('Check that the basket is empty'):
        basket_page.check_cart_is_empty()
