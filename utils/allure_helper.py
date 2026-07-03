import json
import allure


class AllureHelper:

    @staticmethod
    def attach_json(title, data):
        allure.attach(
            json.dumps(data, indent=4),
            name=title,
            attachment_type=allure.attachment_type.JSON
        )

    @staticmethod
    def attach_text(title, text):
        allure.attach(
            str(text),
            name=title,
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def attach_request(method, url, headers=None, payload=None):

        AllureHelper.attach_text(
            "HTTP Method",
            method
        )

        AllureHelper.attach_text(
            "Request URL",
            url
        )

        if headers:
            AllureHelper.attach_json(
                "Request Headers",
                headers
            )

        if payload:
            AllureHelper.attach_json(
                "Request Payload",
                payload
            )

    @staticmethod
    def attach_response(response):

        AllureHelper.attach_text(
            "Status Code",
            response.status_code
        )

        AllureHelper.attach_text(
            "Response Time",
            f"{response.elapsed.total_seconds()} sec"
        )

        try:
            AllureHelper.attach_json(
                "Response Body",
                response.json()
            )
        except Exception:
            AllureHelper.attach_text(
                "Response Body",
                response.text
            )

    @staticmethod
    def attach_log(log_text):
        allure.attach(
            log_text,
            name="Execution Log",
            attachment_type=allure.attachment_type.TEXT
        )