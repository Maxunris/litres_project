import json

from utils.api import LitresAPI
from utils.cheking import Checking

"""Успешный вход"""
def test_successful_login():
    result_post = LitresAPI.post_login()
    Checking.check_status_code(result_post, 200)
    # token = json.loads(result_post.text)
    # print(list(token))
    Checking.check_json_toket(result_post, ['status', 'error', 'payload'])
    Checking.check_json_value(result_post, 'error', None)