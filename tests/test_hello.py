from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_prediction():
    response = client.post("/hello", json={"name": "Susan"})
    assert response.status_code == 200
    assert response.json() == "hello, Susan"
    