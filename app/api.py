from fastapi import FastAPI
from app.model import RantSchema

rants = [
    {
        "id": 1,
        "content": "Hmmmm..... i don't know what to rant yet"
    }
]

users = []

app = FastAPI()


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to my rant page!"}


@app.get("/rants", tags=["rants"])
async def get_rants() -> dict:
    return {"data": rants}


@app.get("/rants/{id}", tags=["rants"])
async def get_single_rant(id: int) -> dict:
    if id > len(rants):
        return {
            "error": "Rant not found with supplied ID"
        }
    for rant in rants:
        if rant["id"] == id:
            return {
                "data": rant
            }
