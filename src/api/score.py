from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ScoreInput(BaseModel):
    feature1: float
    feature2: float

@router.post("/score")
def score(data: ScoreInput):
    result = data.feature1 * data.feature2
    return {"score": result}
    