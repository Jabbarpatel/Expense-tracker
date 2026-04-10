from controllers.users_controller import UsersController
from src.config.config import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


class UsersService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_all_users(self):
        controller = UsersController(self.db)
        users = controller.get_all_users()
        formated_user_list = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "created_at": user.created_at,
            }
            for user in users
        ]
        return formated_user_list
