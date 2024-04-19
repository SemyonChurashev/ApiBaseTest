import pytest
from lib.api_client import ApiClient
from lib.assertions import Assertions
from lib.schema_loader import SchemaLoader
import allure


@allure.epic("WEBSITE/API/NEWS Test")
class TestTerminals:
    @pytest.fixture(scope="module")
    def get_response(self):
        data = ApiClient.get('api/news/')
        return data

    @pytest.fixture(scope="module")
    def get_schema(self):
        schema = SchemaLoader.read_file('news.json')
        return schema

    @allure.title("Test Response HTTP CODE")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("TQ1: Check Http response code for api/news. Expected results 200")
    def test_terminals_code(self, get_response):
        Assertions.assert_http_response_code(get_response, 200)

    @allure.title("Test JSON SCHEMA VALIDATION")
    @allure.tag("Smoke")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("TQ2: Validation JSON SCHEMA")
    def test_json_schema_for_responce(self, get_response, get_schema):
        Assertions.validate_json_schema(get_response, get_schema)

    @allure.description("TQ3: Test pagination parameters for api/news. Expected results\n"
                        "count = results.length"
                        )
    def test_terminals_pagination(self, get_response):
        Assertions.assert_count_and_results(get_response)