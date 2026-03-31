from config.config import Base
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text)
    created_at = Column(TIMESTAMP)

    def __init__(self, name: str, email: str, password: str, created_at):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
