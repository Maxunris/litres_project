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
        print(post_url)
        result_post = HttpMethods.post(post_url, json_correct_data)
        print(result_post.text)
        return result_post

    @staticmethod
    def put_add_to_card():
        load_dotenv()
        json_correct_data = {"art_ids":[66665968]}

        endpoint = "foundation/api/cart/arts/add"
        put_url = base_url + endpoint
        print(put_url)
        result_put = HttpMethods.put(put_url, json_correct_data)
        print(result_put.text)
        return result_put

    @staticmethod
    def put_delete_from_card():
        load_dotenv()
        json_correct_data = {"art_ids":[66665968]}
        endpoint = "foundation/api/cart/arts/remove"
        put_url = base_url + endpoint
        print(put_url)
        result_put = HttpMethods.put(put_url, json_correct_data)
        print(result_put.text)
        return result_put

    @staticmethod
    def get_go_to_audiobooks_page():
        load_dotenv()
        endpoint = "foundation/api/dashboards/dashboard/audiobooks/"
        get_url = base_url + endpoint
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

