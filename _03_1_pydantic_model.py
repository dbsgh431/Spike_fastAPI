from pydantic import BaseModel


class Job(BaseModel):
    id : int
    item : str

    class Config:
        schema_extra = {'example' : {"id":1, "item":"Ex Schema"}}
