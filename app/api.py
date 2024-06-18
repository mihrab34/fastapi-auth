from fastapi import FastAPI, Body
from typing import Dict
from app.auth.auth_handler import sign_jwt
from app.model import RantSchema, UserSchema, UserLoginSchema

rants = [
    {
        "id": 1,
        "content": "Hmmmm..... i don't know what to rant yet"
    }
]

users = []

app = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> Dict:
    return {"message": "Welcome to my rant page!"}


@app.get("/rants", tags=["rants"])
async def get_rants() -> Dict:  # type: ignore
    return {"data": rants}


@app.get("/rants/{id}", tags=["rants"])
async def get_single_rant(id: int) -> Dict:
    if id > len(rants):
        return {
            "error": "Rant not found with supplied ID"
        }
    for rant in rants:
        if rant["id"] == id:
            return {
                "data": rant
            }


@app.post("/rants", tags=["rants"])
async def create_rant(rant: RantSchema) -> Dict:
    rant.id = len(rants) + 1
    rants.append(rant.model_dump())
    return {
        "data": "rant added successfully"
        }


@app.post("/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return sign_jwt(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password == data.password:
            return True
    return False


@app.post("/login", tags=["users"])
async def login_user(user: UserLoginSchema) -> Dict:
    for u in users:
        if u["email"] == user.email and u["password"] == user.password:
            token = sign_jwt(user.email)
            return {
                "data": token
            }
    return {
        "error": "Invalid credentials"
        }
