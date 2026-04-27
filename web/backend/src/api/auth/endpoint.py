from fastapi import APIRouter
from src.services.auth_service import AuthService
from src.api.auth.api_definations import SigninRequest, SigninResponse
from fastapi import Depends
from src.config.config import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["auth"])


def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(db)


@router.post("/login")
def login():
    return {"message": "Login successful"}


@router.post(
    "/signup/{id}",
    response_model=SigninResponse,
    responses={409: {"description": "Failed to sigin"}},
)
def signup(
    id: int,
    signin_request: SigninRequest,
    auth_service: AuthService = Depends(get_auth_service),
):
    name = signin_request.name
    email = signin_request.email
    password = signin_request.password
    auth_service.signin(name, email, password)
    return "success"
