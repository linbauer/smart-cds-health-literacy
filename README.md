# fhir-cds-tool

This is a clinical decision support (CDS) tool designed to integrate with EHRs via SMART on FHIR.

## Structure

- `backend/` – FastAPI app to generate plain-language discharge materials
- `frontend/` – UI (React, or HTML/CSS if simpler)
- `scripts/` – helper CLI scripts (setup, seed, test)
- `public/` – static resources (PDFs, icons)
- `tests/` – unit/integration tests

## Goals

- Deliver health-literate summaries (≤ 6th grade)
- Integrate with Epic/Cerner workflows
- Export multilingual discharge PDFs

## Running Locally

1. Activate your virtual environment:
   ```bash
   source fhir_env/bin/activate
2. Run the app: 
   ```bash
   python3 scripts/run.py
3. Open your browser or use curl to visit:
   http://127.0.0.1:8000/health
   http://127.0.0.1:8000/patients
   http://127.0.0.1:8000/patients/{id}

## Search Example

To search by name and/or birthDate:

```bash
curl "http://127.0.0.1:8000/search?name=Somawathi"
curl "http://127.0.0.1:8000/search?name=John&birthDate=1980-04-15"

### `/education` Endpoint

Returns plain-language educational content for a medical condition.

- ✅ Accepts a `condition` query parameter (`min_length=3`)
- ✅ Loads Markdown files from `test_education_content/`
- ✅ Returns plain text (Markdown-formatted) responses
- ✅ Supports natural language aliases:
  - `"high blood pressure"` → `hypertension.md`
  - `"sugar disease"` → `diabetes.md`
  - `"reactive airway"` → `asthma.md`

#### 📎 Example Requests

```bash
curl "http://127.0.0.1:8000/education?condition=asthma"
curl "http://127.0.0.1:8000/education?condition=high%20blood%20pressure"

# Asthma Education

- Use your inhaler as prescribed.
- Avoid smoke, dust, and cold air.
- Follow up with your doctor within 1 week.

#### 🌐 Language Support

If a localized education file exists, it will be served automatically based on the `Accept-Language` header.

**Example:**

```bash
curl -H "Accept-Language: es" "http://127.0.0.1:8000/education?condition=diabetes"

This will return the content from diabetes.es.md if it exists. If not, the fallback is the default "filename" (e.g. diabetes.md).
