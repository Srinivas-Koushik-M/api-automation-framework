import requests
from core.token_manager import TokenManager

class SessionManager:
    _session = None

    @classmethod
    def get_session(cls):
        if cls._session is None:
            cls._session = requests.Session()
            cls.update_headers()
        return cls._session


    @classmethod
    def update_headers(cls):
        if cls._session is None:
            cls._session = requests.Session()

        auth_header = TokenManager.get_auth_header()

        if auth_header.get("Authorization"):
            cls._session.headers.update(auth_header)


        return cls._session

    @classmethod
    def clear_session(cls):
        if cls._session:
            cls._session.close()

        cls._session = None


