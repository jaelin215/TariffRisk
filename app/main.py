from fastapi import FastAPI
from src.score import router as score_router

app = FastAPI(title="ML Tariff Risk Predictor API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Tariff Risk Predictor API!"}


app.include_router(score_router)