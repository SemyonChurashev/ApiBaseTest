import pytest
from lib.api_client import ApiClient
from lib.assertions import Assertions
import allure


@allure.epic("WEBSITE/API/NEWS Test")
class TestTerminals:
    @pytest.fixture(scope="module")
    def get_response(self):
        data = ApiClient.get('api/news/')
        return data

    @allure.title("Test Response HTTP CODE")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("TQ1: Check Http response code for api/news. Expected results 200")
    def test_terminals_code(self, get_response):
        Assertions.assert_http_response_code(get_response, 200)

    @allure.description("TQ2: Test pagination parameters for api/news. Expected results\n"
                        "count = results.length"
                        )
    def test_terminals_pagination(self, get_response):
        Assertions.assert_count_and_results(get_response)
