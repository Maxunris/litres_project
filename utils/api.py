from dotenv import load_dotenv
from utils.http_methods import HttpMethods
import os

base_url = 'https://api.litres.ru/'
class LitresAPI():
    """Метод для входа с корректными данными"""
    @staticmethod
    def post_successful_login():
        load_dotenv()
        CORRECT_MAIL = os.getenv("CORRECT_MAIL")
        CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
        json_correct_data = {
            "login": CORRECT_MAIL,
            "password": CORRECT_PASSWORD
        }
        endpoint = "foundation/api/auth/login"
        post_url = base_url + endpoint
        print(post_url)
        result_post = HttpMethods.post(post_url, json_correct_data)
        print(result_post.text)
        return result_post

    @staticmethod
    def post_invalid_password():
        load_dotenv()
        CORRECT_MAIL = os.getenv("CORRECT_MAIL")
        INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")
        json_correct_data = {
            "login": CORRECT_MAIL,
            "password": INCORRECT_PASSWORD
        }
        endpoint = "foundation/api/auth/login"
        post_url = base_url + endpoint
        print("постюрл"+post_url)
        result_post = HttpMethods.post(post_url, json_correct_data)
        print("результ пост"+result_post.text)
        return result_post