import requests
import time

from config.config import Config
from core.authentication_manager import AuthenticationManager
from utils.logger import Logger
from utils.allure_helper import AllureHelper


logger = Logger.get_logger(__name__, "api.log")


class BaseAPI:

    @staticmethod
    def request(method, endpoint, auth_required=False, **kwargs):
        url = Config.BASE_URL + endpoint
        response = None

        for attempt in range(1, Config.MAX_RETRIES + 1):

            request_headers = kwargs.get("headers", Config.DEFAULT_HEADERS)
            request_payload = kwargs.get("json", None)

            AllureHelper.attach_request(
                method=method,
                url=url,
                headers=request_headers,
                payload=request_payload
            )

            if auth_required:
                client = AuthenticationManager.authenticate()
                response = client.request(
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

            AllureHelper.attach_response(response)

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

    @staticmethod
    def get(endpoint, auth_required=False, **kwargs):
        return BaseAPI.request("GET", endpoint, auth_required=auth_required, **kwargs)

    @staticmethod
    def post(endpoint, auth_required=False, **kwargs):
        return BaseAPI.request("POST", endpoint, auth_required=auth_required, **kwargs)

    @staticmethod
    def put(endpoint, auth_required=False, **kwargs):
        return BaseAPI.request("PUT", endpoint, auth_required=auth_required, **kwargs)

    @staticmethod
    def patch(endpoint, auth_required=False, **kwargs):
        return BaseAPI.request("PATCH", endpoint, auth_required=auth_required, **kwargs)

    @staticmethod
    def delete(endpoint, auth_required=False, **kwargs):
        return BaseAPI.request("DELETE", endpoint, auth_required=auth_required, **kwargs)












# import requests
# import time
#
# from config.config import Config
# from core.authentication_manager import AuthenticationManager
# from utils.logger import Logger
# from utils.allure_helper import AllureHelper
#
# logger = Logger.get_logger(__name__,"api.log")
#
# class BaseAPI:
#
#     @staticmethod
#     def request(method, endpoint, auth_required=False, **kwargs):
#         url = Config.BASE_URL + endpoint
#         response = None
#
#         for attempt in range(1, Config.MAX_RETRIES + 1):
#
#             if auth_required:
#                 client = AuthenticationManager.authenticate()
#                 response = client.request(
#                     method=method,
#                     url=url,
#                     timeout=Config.TIMEOUT,
#                     **kwargs
#                 )
#             else:
#                 response = requests.request(
#                     method=method,
#                     url=url,
#                     timeout=Config.TIMEOUT,
#                     headers=Config.DEFAULT_HEADERS,
#                     **kwargs
#                 )
#
#             logger.info(
#                 f"""
#                 Attempt : {attempt}
#                 Method : {method}
#                 URL : {url}
#                 Status Code : {response.status_code}
#                 Response Time : {response.elapsed.total_seconds()} sec
#                 """
#             )
#
#             if response.status_code not in Config.RETRY_STATUS_CODES:
#                 break
#
#             if attempt < Config.MAX_RETRIES:
#                 logger.warning(
#                     f"Retrying request. Attempt {attempt}/{Config.MAX_RETRIES}. "
#                     f"Status Code = {response.status_code}"
#                 )
#                 time.sleep(Config.RETRY_DELAY)
#
#         return response
#
#     @staticmethod
#     def get(endpoint, auth_required=False, **kwargs):
#         return BaseAPI.request("GET", endpoint, auth_required=auth_required, **kwargs)
#
#     @staticmethod
#     def post(endpoint, auth_required=False, **kwargs):
#         return BaseAPI.request("POST", endpoint, auth_required=auth_required, **kwargs)
#
#     @staticmethod
#     def put(endpoint, auth_required=False, **kwargs):
#         return BaseAPI.request("PUT", endpoint, auth_required=auth_required, **kwargs)
#
#     @staticmethod
#     def patch(endpoint, auth_required=False, **kwargs):
#         return BaseAPI.request("PATCH", endpoint,auth_required=auth_required, **kwargs)
#
#     @staticmethod
#     def delete(endpoint, auth_required=False, **kwargs):
#         return BaseAPI.request("DELETE", endpoint, auth_required=auth_required, **kwargs)
#
#     # Retry Manager
