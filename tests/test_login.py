from api.auth_api import AuthAPI
from utils.response_validator import ResponseValidator
from utils.api_validator import APIValidator

def test_login():

    response = AuthAPI.login(
        username= "emilys",
        password= "emilyspass"
    )

    APIValidator.validate_success_response(response, 200, required_keys=["accessToken"])

