from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HelloInput(BaseModel):
    name: str

@router.post("/hello")
def greeting(data: HelloInput):
    return f"hello, {data.name}"
    
