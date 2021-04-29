from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_main():
    response = client.get("/", allow_redirects=False)
    assert response.status_code == 307
    assert response.headers["Location"] == "/docs"


def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "🍓 API" in response.text


def test_openapi():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert len(response.json()["paths"]) > 0


def test_uptime():
    response = client.get("/api/v1/uptime")
    assert response.status_code == 200
    assert "up" in response.json()["result"]


def test_speach():
    response = client.post("/api/v1/speach", json={"text": "Hello test"})
    assert response.status_code == 200, response.json()
    assert response.json()["result"] == "I have spoken"
