from playwright.sync_api import Page, expect
import allure
import re
from litres_project.pages.base_page import BasePage


class FilterPage(BasePage):


    @allure.step('Open site')
    def open_popular_page(self):
        self.page.goto(f"popular/")

    @allure.step('Apply "Available by subscription" filter')
    def apply_subscription_filters1(self):
        first_toggle = self.page.locator(".Switcher_toggleWrapper__f7FkR").first
        first_toggle.wait_for(state="visible")
        first_toggle.click()

    @allure.step('Apply "Available in season ticket" filter')
    def apply_subscription_filters2(self):
        third_toggle = self.page.locator(
            "div:nth-child(3) > .Switcher_container__0zipI > .Switcher_children_container__kRhQJ > .Switcher_toggleWrapper__f7FkR")
        third_toggle.wait_for(state="visible")
        third_toggle.click()

    @allure.step('Apply format filters: text and audio')
    def apply_format_filters(self):
        text_filter = self.page.locator("label").filter(has_text="Текст").get_by_role("img")
        text_filter.wait_for(state="visible")
        text_filter.click()

        audio_filter = self.page.locator("label").filter(has_text="Аудио").get_by_role("img")
        audio_filter.wait_for(state="visible")
        audio_filter.click()

    @allure.step('Apply language filter: Russian')
    def apply_language_filter(self):
        russian_filter = self.page.locator("label").filter(has_text="Русский").get_by_role("img")
        russian_filter.wait_for(state="visible")
        russian_filter.click()

    @allure.step('Apply high rating filter')
    def apply_high_rating_filter(self):
        high_rating_filter = self.page.locator("div").filter(
            has_text=re.compile(r"^Высокая оценкаКниги с рейтингом 4 и 5 звёзд$")).get_by_test_id("filter_type--switcher")
        high_rating_filter.wait_for(state="visible")
        high_rating_filter.click()

    @allure.step('Apply promotion discount filter')
    def apply_promotion_discount_filter(self):
        promotion_discount_filter = self.page.locator(
            "div:nth-child(7) > .Switcher_container__0zipI > .Switcher_children_container__kRhQJ > .Switcher_toggleWrapper__f7FkR")
        promotion_discount_filter.wait_for(state="visible")
        promotion_discount_filter.click()

    @allure.step('Apply authors of Litres filter')
    def apply_authors_litres_filter(self):
        authors_litres_filter = self.page.locator(
            "div:nth-child(8) > .Switcher_container__0zipI > .Switcher_children_container__kRhQJ > .Switcher_toggleWrapper__f7FkR")
        authors_litres_filter.wait_for(state="visible")
        authors_litres_filter.click()

    @allure.step('Apply exclusives filter')
    def apply_exclusives_filter(self):
        exclusives_filter = self.page.locator(
            "div:nth-child(9) > .Switcher_container__0zipI > .Switcher_children_container__kRhQJ > .Switcher_toggleWrapper__f7FkR")
        exclusives_filter.wait_for(state="visible")
        exclusives_filter.click()

    @allure.step('Check filters applied')
    def check_filters_applied(self):
        expect(self.page.locator("[id=\"__next\"]")).to_contain_text(
            "Доступно по подпискеДоступно в абонементеТекстАудиоРусскийВысокая оценкаСо скидкой по акцииАвторы ЛитресЭксклюзивыСбросить всё")

    @allure.step('Resetting filters')
    def reset_filters(self):
        reset_button = self.page.locator(
            "div:nth-child(2) > div > .Chips_chipsElement__inner__Nqz_T > .Chips_chipsElement__close__yhqtE")
        reset_button.wait_for(state="visible")
        reset_button.click()
