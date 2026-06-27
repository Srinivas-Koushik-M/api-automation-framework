from core.token_manager import TokenManager
from core.session_manager import SessionManager
from api.auth_api import AuthAPI
from core.user_manager import UserManager

class AuthenticationManager:

    @classmethod
    def authenticate(cls, role="admin"):
        if TokenManager.get_access_token() is None or TokenManager.is_token_expired():
            credentials = UserManager.get_credentials(role)
            AuthAPI.login(
                username=credentials["username"],
                password=credentials["password"]
            )
            SessionManager.update_headers()
        return SessionManager.get_session()



