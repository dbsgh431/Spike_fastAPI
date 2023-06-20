from fastapi import APIRouter, Path, FastAPI
from _03_1_pydantic_model import Job, Job_item 
from _03_3_pydantic_nested_model import Description

app = FastAPI()
router = APIRouter()
job_router = APIRouter()
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

# update 기능 설정
@router.put("/job/{job_id}")
async def update_job(job_info : Job_item, job_id:int =Path(..., title="The Id of the job to be updated")) -> dict:
    for job in job_list:
        if job.id == job_id:
            job.item = job_info.item
            return {
                "message" : "Jobs updated successfully!"
            }
    return {
        "message" :  "Job with supplied Id doesn't exist"
    }
        
# delete 기능 설정
@router.delete("/job/{job_id}")
async def delete_single_job(job_id:int =Path(..., title="The Id of the job to be updated")) -> dict:
    for idx, job in enumerate(job_list):
        if job.id == job_id:
            job_list.pop(idx)
            return {
                "message" : "Jobs deleted successfully!"
            }
    return {
        "message" :  "Job with supplied Id doesn't exist"
    }
    
# delete(all) 기능 설정    
@router.delete("/job")
async def delete_all_jobs() -> dict:
    job_list.clear()
    return {
            "message" :  "Jobs deleted successfully!"
        }

@job_router.get("/jobs")
async def retrieve_job() -> dict:
    return {
        "jobs": job_list
    }
        
app.include_router(router)
app.include_router(job_router)