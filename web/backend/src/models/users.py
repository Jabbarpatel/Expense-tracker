from src.config.config import Base
from sqlalchemy import Integer, String, Text, TIMESTAMP, func, orm


class Users(Base):
    __tablename__ = "users"

    id: orm.Mapped[int] = orm.mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: orm.Mapped[str] = orm.mapped_column(String(50), nullable=False)
    email: orm.Mapped[str] = orm.mapped_column(String(100), nullable=False)
    password: orm.Mapped[str] = orm.mapped_column(Text)
    created_at: orm.Mapped[str] = orm.mapped_column(
        TIMESTAMP, server_default=func.now()
    )

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
