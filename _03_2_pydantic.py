from fastapi import APIRouter
from _03_1_pydantic import Job

router = APIRouter()

job_list = []

@router.post("/job")
async def add_db(job: Job) -> dict:
    job_list.append(job)
    return {
        'message' : "Data added successfully!"}
    

@router.get("/job")
async def retreive_dbs() -> dict:
    return {
        "list" : job_list
    }