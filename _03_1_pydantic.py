from pydantic import BaseModel


class Job(BaseModel):
    id : int
    item : str

