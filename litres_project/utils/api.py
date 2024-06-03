from dotenv import load_dotenv
import os
from litres_project.utils.requests_helper import api_request


class LitresAPI:

    @staticmethod
    def post_successful_login(base_api_url):
        load_dotenv()
        CORRECT_MAIL = os.getenv("CORRECT_MAIL")
        CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD")
        json_correct_data = {
            "login": CORRECT_MAIL,
            "password": CORRECT_PASSWORD
        }
        endpoint = "foundation/api/auth/login"
        response_login = api_request(base_api_url, endpoint, 'POST', json_correct_data)
        return response_login

    @staticmethod
    def post_invalid_password(base_api_url):
        load_dotenv()
        CORRECT_MAIL = os.getenv("CORRECT_MAIL")
        INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD")
        json_correct_data = {
            "login": CORRECT_MAIL,
            "password": INCORRECT_PASSWORD
        }
        endpoint = "foundation/api/auth/login"
        response_login = api_request(base_api_url, endpoint, 'POST', json_correct_data)
        return response_login

    @staticmethod
    def put_add_to_card(base_api_url):
        json_correct_data = {"art_ids": [66665968]}

        endpoint = "foundation/api/cart/arts/add"
        response_add = api_request(base_api_url, endpoint, 'PUT', json_correct_data)
        return response_add

    @staticmethod
    def put_delete_from_card(base_api_url):
        json_correct_data = {"art_ids": [66665968]}
        endpoint = "foundation/api/cart/arts/remove"
        response_delete = api_request(base_api_url, endpoint, 'PUT', json_correct_data)
        return response_delete

    @staticmethod
    def get_go_to_audiobooks_page(base_api_url):
        endpoint = "foundation/api/dashboards/dashboard/audiobooks/"
        response_audiobook = api_request(base_api_url, endpoint, 'GET')
        return response_audiobook


litres_api = LitresAPI()
