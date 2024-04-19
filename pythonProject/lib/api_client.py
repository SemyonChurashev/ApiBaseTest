import requests
from lib.logger import Logger
import allure
from environment import ENV_OBJECT


class ApiClient:
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"Post request for {url}"):
            return ApiClient._send(url, data, headers, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request for {url}"):
            return ApiClient._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request for {url}"):
            return ApiClient._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request for {url}"):
            return ApiClient._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{ENV_OBJECT.get_base_url()}{url}"
        _TIMEOUT = 5
        if headers is None:
            headers = {
                'Content-Type': 'application/json; charset=utf-8'
            }
        if cookies is None:
            cookies = {}

        Logger.add_request(url, data, headers, cookies, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers, cookies=cookies, timeout=_TIMEOUT)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers, cookies=cookies, timeout=_TIMEOUT)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers, cookies=cookies, timeout=_TIMEOUT)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers, cookies=cookies, timeout=_TIMEOUT)
        else:
            raise Exception(f"Wrong HTTP method -> {method} was received")

        Logger.add_response(response)

        return response
