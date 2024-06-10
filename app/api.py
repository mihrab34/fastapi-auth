from fastapi import FastAPI
from app.model import RantSchema

app = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to my rant page!"}


rants = [
    {
        "id": 1,
        "content": "This is a rant secured with pyJWT and Pydantic",
    }
]
