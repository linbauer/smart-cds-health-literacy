from fastapi import APIRouter, HTTPException, Query
import requests
from typing import List, Optional
from app.schemas import SimplifiedPatient

router = APIRouter()
FHIR_SERVER = "https://hapi.fhir.org/baseR4"


@router.get("/patients", response_model=List[SimplifiedPatient])
def get_patients():
    response = requests.get(f"{FHIR_SERVER}/Patient?_count=5&_format=json")
    bundle = response.json()
    entries = bundle.get("entry", [])

    patients = []
    for entry in entries:
        resource = entry.get("resource", {})
        try:
            name_parts = resource.get("name", [{}])[0]
            full_name = " ".join(
                name_parts.get("given", []) + [name_parts.get("family", "")]
            ).strip()
            patient = SimplifiedPatient(
                full_name=full_name, birthDate=resource.get("birthDate")
            )
            patients.append(patient)
        except Exception:
            continue  # Skip malformed entries
    return patients


@router.get("/patients/{patient_id}", response_model=SimplifiedPatient)
def get_patient_by_id(patient_id: str):
    url = f"{FHIR_SERVER}/Patient/{patient_id}?_format=json"
    response = requests.get(url)
    resource = response.json()

    try:
        name_parts = resource.get("name", [{}])[0]
        full_name = " ".join(
            name_parts.get("given", []) + [name_parts.get("family", "")]
        ).strip()
        return SimplifiedPatient(
            full_name=full_name, birthDate=resource.get("birthDate")
        )
    except Exception:
        raise HTTPException(status_code=404, detail="Invalid patient record")


@router.get("/health", tags=["System"])
def health_check():
    return {"status": "ok"}


@router.get("/search", response_model=List[SimplifiedPatient])
def search_patients(
    name: Optional[str] = Query(
        None, min_length=2, max_length=50, description="Patient's given or family name"
    ),
    birthDate: Optional[str] = Query(
        None,
        pattern=r"^\d{4}-\d{2}-\d{2}$",
        description="Birth date in YYYY-MM-DD format",
    ),
):
    url = f"{FHIR_SERVER}/Patient?_count=10&_format=json"

    if name:
        url += f"&name={name}"
    if birthDate:
        url += f"&birthdate={birthDate}"

    response = requests.get(url)
    bundle = response.json()
    entries = bundle.get("entry", [])

    results = []
    for entry in entries:
        resource = entry.get("resource", {})
        name_parts = resource.get("name", [{}])[0]
        full_name = " ".join(
            name_parts.get("given", []) + [name_parts.get("family", "")]
        ).strip()

        if name and name.lower() not in full_name.lower():
            continue  # filter by name locally (FHIR match is partial)

        results.append(
            SimplifiedPatient(full_name=full_name, birthDate=resource.get("birthDate"))
        )

    return results
