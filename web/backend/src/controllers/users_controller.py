from config.config import get_db
from fastapi import Depends
from sqlalchemy.orm import Session


class UsersController:
    def __init__(self, db: Session = Depends(get_db)):
        self.session = db

    def get_all_users(self):
        pass
