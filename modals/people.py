from pydantic import BaseModel

class People(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    