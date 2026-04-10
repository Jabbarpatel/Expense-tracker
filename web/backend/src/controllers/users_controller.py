from src.config.config import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from src.models.users import Users
from typing import Optional


class UsersController:
    def __init__(self, db: Session):
        self.session = db

    def get_user_by_name(self, name: str) -> Users:
        return self.session.query(Users).filter(Users.name == name).first()

    def signin_user(self, user_name: str, email: str, password: str) -> None:
        new_user = Users(name=user_name, email=email, password=password)
        self.session.add(new_user)
        self.session.commit()

    def get_all_users(self) -> list[Users]:
        return self.session.query(Users).all()
