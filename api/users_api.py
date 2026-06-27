from api.base_api import BaseAPI

class UsersAPI:

    @staticmethod
    def get_all_users(**kwargs):
        return BaseAPI.get("/users", **kwargs)

    @staticmethod
    def get_user_by_id(user_id, **kwargs):
        return BaseAPI.get(f"/users/{user_id}", **kwargs)

    @staticmethod
    def create_user(payload, **kwargs):
        return BaseAPI.post(
            "/users/add",
            json=payload,
            **kwargs
        )

    @staticmethod
    def update_user(user_id, payload, **kwargs):
        return BaseAPI.put(
            f"/users/{user_id}",
            json= payload,
            **kwargs
        )

    @staticmethod
    def patch_user(user_id, payload, **kwargs):
        return BaseAPI.patch(
            f"/users/{user_id}",
            json=payload,
            **kwargs
        )

    @staticmethod
    def delete_user(user_id, **kwargs):
        return BaseAPI.delete(
            f"/users/{user_id}",
            **kwargs
        )
