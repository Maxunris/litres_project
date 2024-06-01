import os
from dotenv import load_dotenv
from playwright.sync_api import Page
import allure
from litres_project.pages.filter_page import FilterPage

load_dotenv()

@allure.title("Test other filter")
def test_filter(page: Page, base_url):
    filter_page = FilterPage(page)

    with allure.step('Open site'):
        filter_page.open_popular_page(base_url)

    with allure.step('Apply "Available by subscription" filter'):
        filter_page.apply_subscription_filters1()

    with allure.step('Apply "Available in season ticket" filter'):
        filter_page.apply_subscription_filters2()

    with allure.step('Apply format filters: text and audio'):
        filter_page.apply_format_filters()

    with allure.step('Apply language filter: Russian'):
        filter_page.apply_language_filter()

    with allure.step('Apply high rating filter'):
        filter_page.apply_high_rating_filter()

    with allure.step('Apply promotion discount filter'):
        filter_page.apply_promotion_discount_filter()

    with allure.step('Apply authors of Litres filter'):
        filter_page.apply_authors_litres_filter()

    with allure.step('Apply exclusives filter'):
        filter_page.apply_exclusives_filter()

    with allure.step('Check filters applied'):
        filter_page.check_filters_applied()

    with allure.step('Resetting filters'):
        filter_page.reset_filters()
