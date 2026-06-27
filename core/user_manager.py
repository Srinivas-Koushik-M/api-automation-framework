from config.users import USERS

class UserManager:

    @staticmethod
    def get_credentials(role):
        if role not in USERS:
            raise ValueError(f"User role '{role}' not found in users config")

        return USERS[role]