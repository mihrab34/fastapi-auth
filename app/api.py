from fastapi import FastAPI
from typing import Dict
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
async def read_root() -> Dict:
    return {"message": "Welcome to my rant page!"}


@app.get("/rants", tags=["rants"])
async def get_rants() -> list(dict):  # type: ignore
    return rants
    """
    Get all the rants.

    Returns:
        dict: A dictionary containing the rants data.
    """


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
