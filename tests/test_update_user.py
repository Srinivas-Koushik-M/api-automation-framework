from api.users_api import UsersAPI
from utils.api_validator import APIValidator

def test_update_user():
    user_id = 1
    payload = {
        "firstName": "John",
        "lastName": "Doe",
        "age": 18
    }

    response = UsersAPI.update_user(
        user_id=user_id,
        payload=payload
    )

    APIValidator.validate_success_response(
        response,
        200,
        required_keys=["id"],
        expected_fields=payload
    )

