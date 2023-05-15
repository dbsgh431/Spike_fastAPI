from fastapi import APIRouter

router = APIRouter()

db_list = []

@router.post("/post")
async def add_db(data: dict) -> dict:
    db_list.append(data)
    return {
        'message' : "Data added successfully!"}
    

@router.get("/get")
async def retreive_dbs() -> dict:
    return {
        "list" : db_list
    }