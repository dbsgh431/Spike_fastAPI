from fastapi import APIRouter, Path
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
async def add_job(job: Job) -> dict:
    job_list.append(job)
    return {
        'message' : "Data added successfully!"}
    

@router.get("/job")
async def retreive_jobs() -> dict:
    return {
        "list" : job_list
    }

# job_id를 통해 추가적인 경로 설정
@router.get("/job/{job_id}")
async def get_single_job(job_id:int = Path(...,title='The ID of the job to retrieve.')) -> dict:
    for job in job_list:
        if job.id == job_id:
            return {
                "job" : job
            }
    
    return {
        "message" : "job with supplied ID doesn't exist"
    }