from pydantic import BaseModel
from typing import List

class Job(BaseModel):
    id : int
    item : str

    class Config:
        schema_extra = {'example' : {"id":1, "item":"Ex Schema"}}

class Job_item(BaseModel):
    item : str

    class Config:
        schema_extra = {
            "example" : {
                "item": "View of job list"
            }
        }

class Jobs(BaseModel):
    jobs : List[Job_item]

    class Config:
        schema_extra = {
            "example" : {
                "jobs": [{"item" : "View of job item"},
                         {"item" : "View of job item"}]
            }
        }
