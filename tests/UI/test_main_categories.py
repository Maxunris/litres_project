import os
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.main_categories_page import NavigationPage

load_dotenv()

@allure.title("Test navigation filters")
def test_navigation_filters(page: Page, base_url):
    nav_page = NavigationPage()

    nav_page.set_page(page)
    nav_page.set_base_url(base_url)

    nav_page.open_popular_page()
    nav_page.go_to_subscription_page()
    nav_page.go_to_promo_code_page()
    nav_page.go_to_new_books_page()
    nav_page.go_to_popular_books_page()
    nav_page.go_to_collections_page()
    nav_page.go_to_audiobooks_page()
    nav_page.go_to_exclusives_page()
    nav_page.go_to_drafts_page()
    nav_page.go_to_podcasts_page()
    nav_page.go_to_comics_page()
    nav_page.go_to_journal_page()
