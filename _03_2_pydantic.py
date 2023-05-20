from fastapi import APIRouter
from _03_1_pydantic_model import Job
from _03_3_pydantic_nested_model import Description

router = APIRouter()

job_list = []
description_list = []


@router.post("/description")
async def add_description(description: Description) -> dict:
    description_list.append(description)
    return {
        'message' : "Data added successfully!"}
    

@router.get("/description")
async def retrieve_description() -> dict:
    return {
        "description_list" : description_list
    }

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