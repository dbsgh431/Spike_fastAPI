from fastapi import FastAPI
from _02_1_APIRouter import router

app = FastAPI()

@app.get("/")
async def hello() -> dict:
    return{
        "message" : "hello"
    }

app.include_router(router)