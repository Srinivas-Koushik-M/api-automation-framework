import allure


def allure_api_test(title, feature, story, severity=allure.severity_level.NORMAL):
    def decorator(func):
        func = allure.title(title)(func)
        func = allure.feature(feature)(func)
        func = allure.story(story)(func)
        func = allure.severity(severity)(func)
        return func

    return decorator