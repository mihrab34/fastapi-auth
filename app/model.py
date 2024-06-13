from pydantic import BaseModel, Field, EmailStr


class RantSchema(BaseModel):
    id: int = Field(default=None)
    content: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "content": "This is a rant page secured with pyJWT and Pydantic"
            }
        }


class UserSchema(BaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@me.com",
                "password": "secret"
            }
        }


class UserLoginSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "johndoe@me.com",
                "password": "secret"
            }
        }
