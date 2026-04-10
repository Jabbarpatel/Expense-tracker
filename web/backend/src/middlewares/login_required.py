from starlette.requests import Request
from src.exceptions.auth_exceptions import (
    MissingAuthHeaderException,
    InvalidTokenException,
)
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../../../.env")

SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key12")
ALGORITHM = "HS256"


def login_required(request: Request):
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        raise MissingAuthHeaderException()

    token = auth_header.split(" ")[1]
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    user_name = payload.get("user_name")
    if not user_name:
        raise InvalidTokenException()
