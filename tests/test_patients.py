# 📄 File: tests/test_patients.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search_by_name():
    response = client.get("/search?name=Somawathi")
    assert response.status_code == 200
    results = response.json()
    assert any("Somawathi" in patient["full_name"] for patient in results)


def test_search_by_birthdate():
    response = client.get("/search?birthDate=1930-01-01")
    assert response.status_code == 200
    results = response.json()
    assert any(patient["birthDate"] == "1930-01-01" for patient in results)


def test_search_no_results():
    response = client.get("/search?name=Zyglorbicus")
    assert response.status_code == 200
    results = response.json()
    assert results == []


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search_valid_input():
    response = client.get("/search?name=Somawathi&birthDate=1930-01-01")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any("full_name" in item for item in data)


def test_search_invalid_name():
    response = client.get("/search?name=A")  # too short
    assert response.status_code == 422  # Unprocessable Entity


def test_search_invalid_birthdate():
    response = client.get("/search?birthDate=04-15-1980")  # bad format
    assert response.status_code == 422
