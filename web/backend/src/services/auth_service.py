from src.controllers.users_controller import UsersController
from src.exceptions.users_execeptions import (
    UserNameAlreadyExistsException,
    UserEmailAlreadyExistsException,
)
from src.utils.hashing import hash_password


class AuthService:
    def __init__(self, db):
        self.db = db

    def signin(self, name: str, password: str, email: str) -> None:
        user_controller = UsersController(self.db)

        user = user_controller.get_user_by_name(name)

        if user.name == name:
            raise UserNameAlreadyExistsException()

        if user.email == email:
            raise UserEmailAlreadyExistsException()

        hashed_password = hash_password(password)
        user_controller.signin_user(name, email, hashed_password)
