import os
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.basket_page import BasketPage

load_dotenv()

@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login(page: Page):
    basket_page = BasketPage()
    base_url = os.getenv('BASE_URL')

    basket_page.set_page(page)
    basket_page.set_base_url(base_url)

    basket_page.open_book_page("aleksandr-duma/graf-monte-kristo-5957159/")
    basket_page.check_book_title("Граф Монте-Кристо")
    basket_page.add_book_to_cart()
    basket_page.close_banner()
    basket_page.go_to_cart()
    basket_page.check_book_in_cart("Граф Монте-Кристо")
    basket_page.delete_book_from_cart()
    basket_page.check_cart_is_empty()
