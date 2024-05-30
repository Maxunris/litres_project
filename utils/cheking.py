"""Методы для проверки ответов запросов"""
import json


class Checking():
    """Метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Статус код - правильный")

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Обязательные поля - корректные")


    """Метод для проверки обязательных полей"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("Значение поля " + field_name + " верное!")
