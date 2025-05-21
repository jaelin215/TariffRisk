from fastapi import APIRouter

router = APIRouter()

@router.get("/question")
def question():
    return {"question": "What is your question?"}