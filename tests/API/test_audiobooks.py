from jsonschema import validate
import json
import allure
from litres_project.utils.api import LitresAPI
from litres_project.utils.cheking import Checking
from litres_project.schema.audiobook_schema import audiobook_schema


@allure.title("Audiobook page")
@allure.tag('positive test')
def test_get_to_audiobook_page(base_api_url):
    result_get = LitresAPI.get_go_to_audiobooks_page(base_api_url)
    with allure.step('Status code=200'):
        Checking.check_status_code(result_get, 200)
    token = json.loads(result_get.text)
    print(list(token))
    with allure.step('The presence of required fields'):
        Checking.check_json_token(result_get, ['status', 'error', 'payload'])
    with allure.step('Сhecking required fields'):
        Checking.check_json_value(result_get, 'error', None)
    with allure.step('Сhecking required fields'):
        assert result_get.json()['payload']['data']['title'] == "Аудиокниги"
    with allure.step('Schema is validate'):
        validate(result_get.json(), audiobook_schema)
