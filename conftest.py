import pytest
import requests
from api.auth_api import AuthAPI
from api.users_api import UsersAPI
from core.context_manager import ContextManager


@pytest.fixture(scope="session")
def auth_session():
    response = AuthAPI.login(
        username="emilys",
        password="emilyspass"
    )

    token = response.json()["accessToken"]
    session = requests.Session()
    session.headers.update(
        {
            "Authorization": f"Bearer {token}"
        }

    )
    return session

@pytest.fixture
def cleanup_user():

    yield

    user_id = ContextManager.get_value("user_id")

    if user_id:
        try:
            UsersAPI.delete_user(user_id)
        except Exception as e:
            logger.error(f"Cleanup failed: {e}")
    ContextManager.clear()




