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
