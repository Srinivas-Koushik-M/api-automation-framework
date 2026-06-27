from api.users_api import UsersAPI
from utils.api_validator import APIValidator

def test_create_user():

    payload = {
        "firstName": "test first name",
        "lastName": "test last name",
        "age": 20
    }

    response = UsersAPI.create_user(payload)

    APIValidator.validate_success_response(
        response=response,
        status_code=201,
        required_keys=["id"],
        expected_fields = payload
    )






    # ResponseValidator.validate_fields(data, payload)

