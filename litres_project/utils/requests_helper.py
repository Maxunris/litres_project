import requests


def api_request(base_api_url, endpoint, method, data=None, headers=None, params=None, cookies=None):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method, url, json=data, params=params, headers=headers, cookies=cookies)
    return response
