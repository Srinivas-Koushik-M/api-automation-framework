from utils.logger import Logger
logger = Logger.get_logger(__name__, "api.log")

class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected_status):
        assert response.status_code == expected_status, (
            f"Expected status code {expected_status}, "
            f"but got {response.status_code}"
        )
    @staticmethod
    def validate_key(response_data, key):
        assert key in response_data, (
            f"key '{key}' not found in response"
        )

    @staticmethod
    def validate_value(response_data, key, value):
        assert response_data.get(key) == value, (
            f"Value '{value}' not found in response"
        )

    @staticmethod
    def validate_list_not_empty(data_list):
        assert len(data_list) > 0, (
            "Expected list to contain data, but it is empty."
        )

    @staticmethod
    def validate_list_size(data_list, expected_size):
        actual_size = len(data_list)
        assert actual_size == expected_size, (
            f"Expected size of list {expected_size}, ",
            f"but got {actual_size}"
        )

    @staticmethod
    def validate_fields(actual_data, expected_data):

        for key, expected_value in expected_data.items():
            actual_value = actual_data.get(key)

            assert actual_value == expected_value, (
                f"Validation field for {key}."
                f"Expected {expected_value}, "
                f"Actual {actual_value}"

            )

    @staticmethod
    def validate_response_time(response, max_response_time=2, strict=True):

        actual_response_time = response.elapsed.total_seconds()
        logger.info(f"Response Time : {actual_response_time:.3f} sec")

        if strict:
            assert actual_response_time <= max_response_time, (
                f"Expected response time <= {max_response_time}s, "
                f"but got {actual_response_time:.3f}s"
            )
        elif actual_response_time > max_response_time:

            logger.warning(
                f"Response time exceeded SLA. "
                f"Expected <= {max_response_time}s "
                f"Actual = {actual_response_time:.3f}s"
            )
