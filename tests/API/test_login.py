from utils.http_methods import HttpMethods
from utils.api import LitresAPI
import os

"""Успешный вход"""
def test_successful_login():
    result_post = LitresAPI.post_login()
    print(result_post)



