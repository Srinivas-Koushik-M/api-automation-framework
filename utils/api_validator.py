from utils.response_validator import ResponseValidator
from utils.schema_validator import SchemaValidator

class APIValidator:

    @staticmethod
    def validate_success_response(
        response,
        status_code,
        required_keys = None,
        schema_path = None,
        expected_fields = None,
        max_response_time = 2
    ):


        ResponseValidator.validate_status_code(response, status_code)
        ResponseValidator.validate_response_time(response, max_response_time)

        data = response.json()

        if required_keys:
            for key in required_keys:
                ResponseValidator.validate_key(data, key)

        if schema_path:
            SchemaValidator.validate_schema(data, schema_path)

        if expected_fields:
            ResponseValidator.validate_fields(data, expected_fields)
