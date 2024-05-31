# conftest.py
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://www.litres.ru/"

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.mark.only_browser("chromium")
def test_visit_example(page, base_url):
    page.goto(base_url)