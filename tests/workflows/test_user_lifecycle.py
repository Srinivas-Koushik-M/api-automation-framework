from api.users_api import UsersAPI
from core.context_manager import ContextManager
from utils.response_validator import ResponseValidator

def test_user_lifecycle(cleanup_user):
    try:
        #Test Create New User
        create_payload = {
            "firstName": "Michael",
            "lastName": "William",
            "age": 20
        }

        # send post request to create new user
        create_response = UsersAPI().create_user(create_payload)
        create_data = create_response.json()

        # validating new user created
        ResponseValidator.validate_status_code(create_response, 201)
        ResponseValidator.validate_key(create_data, "id")
        ResponseValidator.validate_fields(create_data, create_payload)

        # get user id after user created and adding user ID to context manger
        ContextManager.set_value(
            "user_id",
            create_data["id"]
        )


        # Test GET User data
        # get_user_response = UsersAPI.get_user_by_id(
        #     ContextManager.get_value("user_id")
        # )
        #
        # get_user_data = get_user_response.json()
        #
        # # validate user data
        # ResponseValidator.validate_status_code(get_user_response, 200)
        # ResponseValidator.validate_fields(get_user_response, create_payload)


        #Test UPDATE user data
        update_payload = {
            "firstName": "William",
            "lastName": "Michael",
            "age": 22
        }

        update_response = UsersAPI.update_user(
            user_id=ContextManager.get_value("user_id"),
            payload=update_payload
        )

        update_data = update_response.json()

        # validate updated user data
        ResponseValidator.validate_status_code(update_response, 200)
        ResponseValidator.validate_fields(update_data, update_payload)

        #Test Delete User
        delete_response = UsersAPI.delete_user(
            ContextManager.get_value("user_id")
        )

        ResponseValidator.validate_status_code(delete_response, 200)

        #Test get user after deleting
        # get_user_response_after_delete = UsersAPI.get_user_by_id(
        #     ContextManager.get_value("user_id")
        # )
        #
        # ResponseValidator.validate_status_code(get_user_response_after_delete, 204)
        #

    finally:
        user_id = ContextManager.get_value("user_id")

        if user_id:
            #Test Delete User
            try:
                delete_response = UsersAPI.delete_user(user_id)

                if delete_response.status_code not in (200, 204):
                    logger.warning(
                        f"Cleanup failed for user {user_id}. "
                        f"Status: {delete_response.status_code}"
                    )
            except Exception as e:
                logger.error(
                    f"Cleanup exception: {user_id}. "
                )
        ContextManager.clear()







