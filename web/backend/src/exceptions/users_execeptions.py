from src.exceptions.app_exception import AppException


class UserNameAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
            message="User with the given name already exists!", status_code=400
        )


class UserEmailAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
            message="User with the given email already exists!", status_code=400
        )
