import requests
from config.config import Config
from core.token_manager import TokenManager


class AuthAPI:

    @staticmethod
    def login(username, password, **kwargs):

        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(
            url=Config.BASE_URL + "/auth/login",
            json=payload,
            headers=Config.DEFAULT_HEADERS,
            timeout=Config.TIMEOUT,
            **kwargs
        )

        data = response.json()

        TokenManager.set_tokens(
            access_token=data.get("access_token"),
            refresh_token=data.get("refresh_token"),
            expires_in=data.get("expires_in"),
            token_type=data.get("token_type")
        )

        return response


