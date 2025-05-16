from fastapi import FastAPI
from app.routers import patients, education

app = FastAPI()

# Register routers
app.include_router(patients.router)
app.include_router(education.router)


@app.get("/")
def root():
    return {"message": "FHIR CDS Tool backend is live!"}
