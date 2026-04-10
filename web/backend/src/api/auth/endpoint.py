from fastapi import APIRouter
from src.services.auth_service import AuthService
from src.api.auth.api_definations import SigninRequest
from fastapi import Depends
from src.config.config import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["auth"])


def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(db)


@router.post("/login")
def login():
    # Implement login endpoint logic here
    return {"message": "Login successful"}


@router.post("/signup")
def signup(
    signin_request: SigninRequest, auth_service: AuthService = Depends(get_auth_service)
):
    name = signin_request.name
    email = signin_request.email
    password = signin_request.password
    print(name, email, password)
    auth_service.signin(name, email, password)
    return "success"
