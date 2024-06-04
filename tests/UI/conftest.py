import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session", autouse=True)
def base_url():
    return "https://www.litres.ru/"

@pytest.fixture()
def page(context):
    page = context.new_page()
    page.set_viewport_size({"width": 1980, "height": 1080})
    yield page
# @pytest.fixture(scope="session")
# def test_visit_example(page, base_url):
#     page.goto(base_url)
