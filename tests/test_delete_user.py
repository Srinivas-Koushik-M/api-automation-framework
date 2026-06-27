from api.users_api import UsersAPI
from utils.response_validator import ResponseValidator
from utils.api_validator import APIValidator

def test_delete_user():
    user_id = 1

    response = UsersAPI.delete_user(user_id)

    APIValidator.validate_success_response(response, 200, required_keys=["id"])

    ResponseValidator.validate_value(response.json(), "id", user_id)