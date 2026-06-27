import time

class TokenManager:
    _access_token = None
    _refresh_token = None
    _expires_at = None
    _token_type = "Bearer"

    @classmethod
    def set_tokens(cls, access_token, refresh_token=None, expires_in=None, token_type="Bearer"):
        cls._access_token = access_token
        cls._refresh_token = refresh_token
        cls._token_type = token_type

        if expires_in:
            cls._expires_at = time.time() + expires_in

    @classmethod
    def get_access_token(cls):
        return cls._access_token

    @classmethod
    def get_refresh_token(cls):
        return cls._refresh_token

    @classmethod
    def get_token_type(cls):
        return cls._token_type

    @classmethod
    def is_token_expired(cls, buffer_seconds=60):

        if cls._expires_at is None:
            return False

        return time.time() > cls._expires_at - buffer_seconds

    @classmethod
    def get_auth_header(cls):
        return {
            "Authorization": f"{cls._token_type} {cls._refresh_token}"
        }







