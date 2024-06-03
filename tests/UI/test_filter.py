from playwright.sync_api import Page
import allure
from litres_project.pages.filter_page import FilterPage


@allure.title("Test other filter")
def test_filter(page: Page, base_url):
    filter_page = FilterPage()

    filter_page.set_page(page)
    filter_page.set_base_url(base_url)

    filter_page.open_popular_page()
    filter_page.apply_subscription_filters1()
    filter_page.apply_subscription_filters2()
    filter_page.apply_format_filters()
    filter_page.apply_language_filter()
    filter_page.apply_high_rating_filter()
    filter_page.apply_promotion_discount_filter()
    filter_page.apply_authors_litres_filter()
    filter_page.apply_exclusives_filter()
    filter_page.check_filters_applied()
    filter_page.reset_filters()
