import fastapi
from pydantic import BaseModel

class Item(BaseModel):
    item : str
    status : str

class Description(BaseModel):
    id : int 
    item : Item
