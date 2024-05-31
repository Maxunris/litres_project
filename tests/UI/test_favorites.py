import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import allure

load_dotenv()
CORRECT_MAIL = os.getenv("CORRECT_MAIL")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")


@allure.title("successful_login")
@allure.tag('positive test')
def test_favorites(page: Page, base_url):

    with allure.step('Open search'):
        page.goto(base_url + "search/?q=граф%20монте%20кристо")

    with allure.step('Adding a book to favorites'):
        page.locator(".LikeButton_likeButton__hix0G").first.click()

    with allure.step('Go to favorites'):
        page.get_by_role("link", name="icon-favorite 1 Отложенные").click()

    with allure.step('Checking the number of books'):
        expect(page.get_by_test_id("navigation__tabsList")).to_contain_text("Отложено1")

    with allure.step('Check the title of the book and the author'):
        expect(page.get_by_test_id("art__title").get_by_role("paragraph")).to_contain_text("Граф Монте-Кристо")
        expect(page.get_by_test_id("art__authorName")).to_contain_text("Александр Дюма")

    with allure.step('Deleting a book from favorites'):
        page.get_by_test_id("art__wrapper").get_by_test_id("popover__baseElement").locator("a").click()
        page.get_by_text("Убрать из отложенного").click()

    with allure.step('Check that there are no books in the favorites'):
        expect(page.get_by_test_id("navigation__tabsList")).to_contain_text("Отложено")