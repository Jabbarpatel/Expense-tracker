from fastapi import APIRouter, Depends
from src.middlewares.login_required import login_required

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def test(dep=Depends(login_required)):
    return {"message": "Hello, World!"}
