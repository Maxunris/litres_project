from jsonschema import validate
import json
import allure
from utils.api import LitresAPI
from utils.cheking import Checking
from litres_project.schema.add_to_card_schema import add_to_card_schema
"""Успешный вход"""

@allure.title("Add to card")
@allure.tag('positive test')
def test_add_to_card():
    result_put = LitresAPI.put_add_to_card()
    with allure.step('Status code=200'):
        Checking.check_status_code(result_put, 200)
    token = json.loads(result_put.text)
    print(list(token))
    with allure.step('The presence of required fields'):
        Checking.check_json_token(result_put, ['status', 'error', 'payload'])
    with allure.step('Сhecking required fields'):
        Checking.check_json_value(result_put, 'error', None)
    with allure.step('Сhecking required fields'):
        assert result_put.json()['payload']['data']['added_art_ids'] == [66665968]
    with allure.step('Schema is validate'):
        validate(result_put.json(), add_to_card_schema)

@allure.title("Delete from card")
@allure.tag('positive test')
def test_delete_from_card():
    result_put = LitresAPI.put_delete_from_card()
    with allure.step('Status code=204'):
        Checking.check_status_code(result_put, 204)

