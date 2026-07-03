import allure
from api.auth_api import AuthAPI
from utils.response_validator import ResponseValidator
from utils.api_validator import APIValidator

@allure.title("User Login API")
@allure.description("Verify user can login successfully")
@allure.feature("Login API")
@allure.story("Login API")
@allure.severity(allure.severity_level.CRITICAL)
def test_login():

    response = AuthAPI.login(
        username= "emilys",
        password= "emilyspass"
    )

    APIValidator.validate_success_response(response, 200, required_keys=["accessToken"])

