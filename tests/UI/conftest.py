import pytest

@pytest.fixture(scope="session", autouse=True)
def base_url():
    return "https://www.litres.ru/"

@pytest.fixture(scope="session", autouse=True)
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

# @pytest.fixture(scope="session")
# def test_visit_example(page, base_url):
#     page.goto(base_url)
