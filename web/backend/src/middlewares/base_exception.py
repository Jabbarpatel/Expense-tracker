from fastapi import Request
from fastapi.responses import JSONResponse
from src.exceptions.app_exception import AppException


def base_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, AppException):
        status_code = exc.status_code
        message = exc.message
    else:
        status_code = 500
        message = "Internal server error"

    return JSONResponse(
        status_code=status_code,
        content={"message": message},
    )
