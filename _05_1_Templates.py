from fastapi import APIRouter, Path, HTTPException, status, FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from _03_1_pydantic_model import Job, Job_item

app = FastAPI()
job_router = APIRouter()
job_list = []

templates = Jinja2Templates(directory='templates/')

@job_router.get("/job", response_model=Job_item)
async def retrieve_single_job(request:Request) -> dict:
    return templates.TemplateResponse("job.html", {
        "request": request,
        "jobs" : job_list
    })


@job_router.get("/job/{job_id}")
async def get_single_job(request:Request, job_id: int=Path(..., title="ID of the job to do retrieve"))-> dict:
    for job in job_list:
        if job.id == job_id:
            return templates.TemplateResponse("job.html", {
            "request": request,
            "job" : job
            })
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Job with supplied id does not exist!"
    )

@job_router.put("job/{job_id}")
async def update_job(job_data : Job_item, job_id :int = Path(..., title="ID of the job of to be updated")) -> dict:
    for job in job_list:
        if job.id == job_id:
            job.item = job_data.item
            return {
                "job": "job updated successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Job with supplied id does not exist!"
    ) 

# delete 기능 설정
@job_router.delete("/job/{job_id}")
async def delete_single_job(job_id:int =Path(..., title="The Id of the job to be updated")) -> dict:
    for idx, job in enumerate(job_list):
        if job.id == job_id:
            job_list.pop(idx)
            return {
                "message" : "Jobs deleted successfully!"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Job with supplied id does not exist!"
    ) 

@job_router.post("/job")
async def add_job(request: Request, job : Job=Depends(Job.as_form)):
    job.id = len(job_list) + 1
    job_list.append(job)
    return templates.TemplateResponse("job.html", 
    {
      'request' : request,
      "jobs" : job_list  
    })

app.include_router(job_router)