import os
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.main_categories_page import NavigationPage

load_dotenv()

@allure.title("Test navigation filters")
def test_navigation_filters(page: Page, base_url):
    nav_page = NavigationPage(page)

    with allure.step('Open popular page'):
        nav_page.open_popular_page(base_url)

    with allure.step('Navigate to subscription page'):
        nav_page.go_to_subscription_page()

    with allure.step('Navigate to promo code page'):
        nav_page.go_to_promo_code_page()

    with allure.step('Navigate to new books page'):
        nav_page.go_to_new_books_page()

    with allure.step('Navigate to popular books page'):
        nav_page.go_to_popular_books_page()

    with allure.step('Navigate to collections page'):
        nav_page.go_to_collections_page()

    with allure.step('Navigate to audiobooks page'):
        nav_page.go_to_audiobooks_page()

    with allure.step('Navigate to exclusives page'):
        nav_page.go_to_exclusives_page()

    with allure.step('Navigate to drafts page'):
        nav_page.go_to_drafts_page()

    with allure.step('Navigate to podcasts page'):
        nav_page.go_to_podcasts_page()

    with allure.step('Navigate to comics page'):
        nav_page.go_to_comics_page()

    with allure.step('Navigate to journal page'):
        nav_page.go_to_journal_page()
