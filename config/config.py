import os

class Config:
    BASE_URL = os.getenv(
        "BASE_URL",
        "https://dummyjson.com")
    # BASE_URL = "https://dummyjson.com"
    TIMEOUT = 30
    DEFAULT_HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    USERNAME = "emilys"
    PASSWORD = "emilyspass"

    MAX_RETRIES = 3
    RETRY_DELAY = 2

    RETRY_STATUS_CODES = [
        500,
        502,
        503,
        504
    ]