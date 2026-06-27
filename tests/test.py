import requests
import time

from config.config import Config
from core.authentication_manager import AuthenticationManager
from utils.logger import Logger

logger = Logger.get_logger(__name__, "api.log")


class BaseAPI:

    @staticmethod
    def request(method, endpoint, auth_required=False, **kwargs):
        url = Config.BASE_URL + endpoint
        response = None

        for attempt in range(1, Config.MAX_RETRIES+1):

            if auth_required:
                session = AuthenticationManager.authenticate()
                response = session.request(
                    method=method,
                    url=url,
                    timeout=Config.TIMEOUT,
                    **kwargs
                )
            else:
                response = requests.request(
                    method=method,
                    url=url,
                    timeout=Config.TIMEOUT,
                    headers=Config.DEFAULT_HEADERS,
                    **kwargs
                )

            logger.info(
                f"""
                    Attempt : {attempt}
                    Method : {method}
                    URL : {url}
                    Status Code : {response.status_code}
                    Response Time : {response.elapsed.total_seconds()} sec
                """
            )

            if response.status_code not in Config.RETRY_STATUS_CODES:
                break

            if attempt < Config.MAX_RETRIES:
                logger.warning(
                    f"Retrying request. Attempt {attempt}/{Config.MAX_RETRIES}. "
                    f"Status Code = {response.status_code}"
                )
                time.sleep(Config.RETRY_DELAY)
        return response