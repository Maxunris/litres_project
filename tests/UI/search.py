import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
import allure

load_dotenv()
CORRECT_MAIL = os.getenv("CORRECT_MAIL")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")


@allure.title("Search for an existing book")
def correct_search(page: Page, base_url):
    with allure.step('Open site'):
        page.goto(base_url)

    with allure.step('Enter correct name book'):
        page.get_by_test_id("search__input").fill("Граф монте кристо")
        page.get_by_test_id("search__input").press("Enter")

    with allure.step('Checking the title and author'):
        expect(page.get_by_test_id("search__content--wrapper")).to_contain_text("Граф Монте-Кристо")
        expect(page.get_by_test_id("search__content--wrapper")).to_contain_text("Александр Дюма")

@allure.title("Search for a non-existent book")
def incorrect_search(page: Page, base_url):
    with allure.step('Open site'):
        page.goto(base_url)

    with allure.step('Enter incorrect name book'):
        page.get_by_test_id("search__input").fill("парорарампам")
        page.get_by_test_id("search__input").press("Enter")

    with allure.step('Checking the message that the book was not found'):
        expect(page.locator("[id=\"__next\"]")).to_contain_text("ничего не найденоПопробуйте изменить запрос")
