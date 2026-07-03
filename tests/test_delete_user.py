import allure
from api.users_api import UsersAPI
from utils.response_validator import ResponseValidator
from utils.api_validator import APIValidator


@allure.title("Delete user API")
@allure.description("Verify that a user can be deleted successfully")
@allure.feature("User API")
@allure.story("Delete user")
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_user():
    user_id = 1

    response = UsersAPI.delete_user(user_id)

    APIValidator.validate_success_response(response, 200, required_keys=["id"])

    ResponseValidator.validate_value(response.json(), "id", user_id)