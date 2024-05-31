from jsonschema import validate
import allure
from utils.api import LitresAPI
from utils.cheking import Checking
from litres_project.schema.successful_login_schema import login
from litres_project.schema.invalid_password_schema import invalid_login
"""Успешный вход"""

@allure.title("successful_login")
@allure.tag('positive test')
def test_successful_login():
    result_post = LitresAPI.post_successful_login()
    with allure.step('Status code=200'):
        Checking.check_status_code(result_post, 200)
    # token = json.loads(result_post.text)
    # print(list(token))
    with allure.step('The presence of required fields'):
        Checking.check_json_token(result_post, ['status', 'error', 'payload'])
    with allure.step('Сhecking required fields'):
        Checking.check_json_value(result_post, 'error', None)
    with allure.step('Schema is validate'):
        validate(result_post.json(), login)

"""Неверный пароль"""

@allure.title("invalid password")
@allure.tag('negative test')
def test_invalid_password():
    result_post = LitresAPI.post_invalid_password()
    with allure.step('Status code=401'):
        Checking.check_status_code(result_post, 401)
    with allure.step('The presence of required fields'):
        Checking.check_json_token(result_post, ['status', 'error'])
    with allure.step('Сhecking required fields'):
        assert result_post.json()['error']['type'] == "Unauthorized"
        assert result_post.json()['error']['title'] == "Incorrect user data"
        """
            Ps для Алекса. Я смог найти только такое решение пока. Но если можно использовать функцию 
            check_json_value для указания type и title, буду очень рад услышать как именно)
             Да и в целом было бы интересно услышать Ваше мнение, в правильном ли направлении работаю^^
        """

    with allure.step('Schema is validate'):
        validate(result_post.json(), invalid_login)
    # print("gehsadasf "+result_post.json()['error']['type'])
    # Checking.check_json_value(result_post, 'type', "Unauthorized")
    # Checking.check_json_value(result_post, 'title ', "Incorrect user data")

