from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction():
    response = client.post("/score", json={"feature1": 1, "feature2": 2})
    assert response.status_code == 200
    assert response.json()["score"] == 2