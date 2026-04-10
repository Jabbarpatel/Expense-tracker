from src.exceptions.app_exception import AppException


class MissingAuthHeaderException(AppException):
    def __init__(self):
        super().__init__(message="Authorization header is missing!", status_code=401)


class InvalidTokenException(AppException):
    def __init__(self):
        super().__init__(message="Invalid token!", status_code=401)
