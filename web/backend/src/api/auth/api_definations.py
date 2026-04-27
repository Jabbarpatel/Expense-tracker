from pydantic import BaseModel, Field


class SigninRequest(BaseModel):
    name: str = Field(example="Jabbar Patel")
    email: str = Field(example="Jabbar@email.com")
    password: str = Field(example="Jabbar@123")


class SigninResponse(BaseModel):
    token: str = Field(example="token")
