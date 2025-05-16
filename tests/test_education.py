from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_education_known_condition():
    response = client.get("/education?condition=asthma")
    assert response.status_code == 200
    assert "Asthma Education" in response.text
    assert "- Use your inhaler" in response.text


def test_education_unknown_condition():
    response = client.get("/education?condition=eczema")
    assert response.status_code == 404
    assert "No education material" in response.text


def test_education_no_condition():
    response = client.get("/education")
    assert response.status_code == 200
    assert "Welcome to the Health Education Endpoint" in response.text


def test_education_short_condition():
    response = client.get("/education?condition=ab")
    assert response.status_code == 422  # min_length=3 enforced


def test_fhir_term_diabetes_type2():
    response = client.get("/education?condition=type%202%20diabetes%20mellitus")
    assert response.status_code == 200
    assert "Diabetes" in response.text or "diabetes" in response.text


def test_fhir_term_essential_hypertension():
    response = client.get("/education?condition=essential%20hypertension")
    assert response.status_code == 200
    assert "Hypertension" in response.text


def test_indexed_condition_exact_match():
    response = client.get("/education?condition=asthma")
    assert response.status_code == 200
    assert "Asthma" in response.text


def test_indexed_condition_alias():
    response = client.get("/education?condition=high blood pressure")
    assert response.status_code == 200
    assert (
        "pressure" in response.text.lower() or "hypertension" in response.text.lower()
    )


def test_indexed_condition_fhir_term():
    response = client.get("/education?condition=type 2 diabetes mellitus")
    assert response.status_code == 200
    assert "Diabetes" in response.text


def test_indexed_condition_not_found():
    response = client.get("/education?condition=eczema")
    assert response.status_code == 404
    assert "No education material" in response.text
