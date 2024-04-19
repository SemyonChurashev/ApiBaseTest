from requests import Response
import json
from jsonschema import validate
from jsonschema import ValidationError


class Assertions:

    @staticmethod
    def assert_count_and_results(response: Response):
        response_as_dict = response.json()
        count_value = response_as_dict["count"]
        results_value = len(response_as_dict["results"])
        assert count_value == results_value, f"Test failed, expected: {count_value}, but got: {results_value}"

    @staticmethod
    def assert_http_response_code(response: Response, expected_http_code):
        assert response.status_code == expected_http_code, (f"Test failed, expected : {expected_http_code}, "
                                                            f"but got: {response.status_code}")

    @staticmethod
    def validate_json_schema(response: Response, schema):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response body is not in JSON format. Body contains: {response.text}"
        try:
            validate(instance=response_as_dict, schema=schema)
        except ValidationError as ex:
            assert False, f"JSON validation error: {ex}"
        assert True
