import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import allure
from litres_project.pages.favorites_page import FavoritesPage

load_dotenv()

@allure.title("successful_login")
@allure.tag('positive test')
def test_favorites(page: Page, base_url):
    favorites_page = FavoritesPage(page)

    with allure.step('Open search'):
        favorites_page.open_search_page(base_url, "граф%20монте%20кристо")

    with allure.step('Adding a book to favorites'):
        favorites_page.add_book_to_favorites()

    with allure.step('Go to favorites'):
        favorites_page.go_to_favorites()

    with allure.step('Checking the number of books'):
        favorites_page.check_number_of_books(1)

    with allure.step('Check the title of the book and the author'):
        favorites_page.check_book_details("Граф Монте-Кристо", "Александр Дюма")

    with allure.step('Deleting a book from favorites'):
        favorites_page.remove_book_from_favorites()

    with allure.step('Check that there are no books in the favorites'):
        favorites_page.check_no_books_in_favorites()
