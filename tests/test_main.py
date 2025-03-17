from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/1", json={"name": "Test Item", "description": "Test Description", "price": 10.99})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_read_item():
    client.post("/items/2", json={"name": "Test Item 2", "description": "Test Description 2", "price": 20.99})
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item 2"