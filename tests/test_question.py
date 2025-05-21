from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_question():
    response = client.get("/question")
    data = response.json()
    assert response.status_code == 200
    assert data == {"question": "What is your question?"}