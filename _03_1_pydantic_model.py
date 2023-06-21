from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form

class Job(BaseModel):
    id : Optional[int]
    item : str

    @classmethod
    def as_form(
        cls,
        item : str = Form(...)
    ):
        return cls(item=item)
    

class Job_item(BaseModel):
    item : str

    class Config:
        schema_extra = {
            "example" : {
                "item": "View of job list"
            }
        }

class Jobs(BaseModel):
    jobs : List[Job]

    class Config:
        schema_extra = {
            "example" : {
                "jobs": [{"item" : "View of job item"},
                         {"item" : "View of job item"}]
            }
        }
