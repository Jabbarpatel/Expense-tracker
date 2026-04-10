from fastapi import FastAPI
from src.middlewares.base_exception import base_exception_handler
from src.exceptions.app_exception import AppException
from src.api.users.endpoint import router as users_router
from src.api.auth.endpoint import router as auth_router

app = FastAPI()

# REGISTER ENDPOINTS HERE
app.include_router(auth_router, prefix="/api")
app.include_router(users_router, prefix="/api")

app.add_exception_handler(Exception, base_exception_handler)
app.add_exception_handler(AppException, base_exception_handler)
