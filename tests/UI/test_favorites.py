import os
import time
from litres_project.pages.base_page import BasePage

from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.favorites_page import FavoritesPage

load_dotenv()

@allure.title("successful_login")
@allure.tag('positive test')
def test_favorites(page: Page):
    favorites_page = FavoritesPage()
    base_url = os.getenv('BASE_URL')

    favorites_page.set_page(page)
    favorites_page.set_base_url(base_url)

    favorites_page.open_search_page("граф%20монте%20кристо")
    favorites_page.add_book_to_favorites()
    favorites_page.go_to_favorites()
    favorites_page.check_number_of_books(1)
    favorites_page.check_book_details("Граф Монте-Кристо", "Александр Дюма")
    favorites_page.remove_book_from_favorites()
    favorites_page.check_no_books_in_favorites()
