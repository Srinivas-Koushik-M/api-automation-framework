import pytest

from api.users_api import UsersAPI
from utils.api_validator import APIValidator
from utils.response_validator import ResponseValidator
from utils.schema_validator import SchemaValidator


@pytest.mark.parametrize(
    "limit, skip",
        [
            (5, 0) ,
            (5, 5),
            (10, 5),
            (15, 10)
        ]
)
def test_get_users_with_limit(limit, skip):
    response = UsersAPI().get_all_users(
        params={
            "limit": limit,
            "skip": skip
        }
    )

    # ResponseValidator.validate_status_code(response, 200)
    APIValidator.validate_success_response(
        response,
        200,
        required_keys=["users"]

    )
    data = response.json()

    # ResponseValidator.validate_key(data, "users")
    ResponseValidator.validate_list_not_empty(data["users"])
    ResponseValidator.validate_list_size(data["users"], limit)


@pytest.mark.parametrize(
    "user_id",
    [1, 5, 10]
)
def test_get_user_by_id(user_id):

    response = UsersAPI.get_user_by_id(user_id)

    APIValidator.validate_success_response(
        response,
        200,
        required_keys=["id"],
        schema_path = "schemas/user_schema.json"
    )
    ResponseValidator.validate_value(response.json(), "id", user_id)

    # data = response.json()
    #
    #
    # assert data["id"] == user_id


# def test():
#     a = {
#         "id": 1,
#     }
#     print(type(a))



# import requests
#
# response = requests.get("http://127.0.0.1:5000/users")





# import requests
#
#
# def test_all_users():
#
#     response = requests.get("https://dummyjson.com/users")
#
#     assert response.status_code == 200
#
#     data = response.json()
#
#     assert "users" in data
#     assert len(data["users"]) > 0