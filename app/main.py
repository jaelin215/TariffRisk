from fastapi import FastAPI
from src.api.score import router as score_router
from src.api.hello import router as hello_router
from src.api.question import router as question_router

app = FastAPI(title="ML Tariff Risk Predictor API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Tariff Risk Predictor API!"}

app.include_router(score_router)
app.include_router(hello_router)
app.include_router(question_router)