import allure

from api.users_api import UsersAPI
from utils.api_validator import APIValidator
from utils.allure_decorator import allure_api_test


@allure_api_test(
    title="Create User API",
    feature="Users API",
    story="Create User",
    severity=allure.severity_level.CRITICAL
)
def test_create_user():

    with allure.step("Create request payload"):
        payload = {
            "firstName": "test first name",
            "lastName": "test last name",
            "age": 20
        }

    with allure.step("Send Create User request"):
        response = UsersAPI.create_user(payload)

    with allure.step("Validate response"):
        APIValidator.validate_success_response(
            response=response,
            status_code=201,
            required_keys=["id"],
            expected_fields=payload
        )