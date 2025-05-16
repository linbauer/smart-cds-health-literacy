# 📁 File: ~/Projects/fhir_app/app/routers/education.py

from fastapi import APIRouter, Query, Request
from fastapi.responses import PlainTextResponse
from typing import Optional
import os
import json

from app.utils.normalize import normalize_condition_term

router = APIRouter()

# ⚠️ TEMP: Using test markdown content only
EDU_DIR = os.path.join(os.path.dirname(__file__), "../../test_education_content")
INDEX_PATH = os.path.join(os.path.dirname(__file__), "../../content_index.json")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    CONTENT_INDEX = json.load(f)


@router.get("/education", response_class=PlainTextResponse)
async def get_education(
    request: Request,
    condition: Optional[str] = Query(None, min_length=3, pattern=r"^[\w\s\-]+$"),
):
    if condition:
        normalized = normalize_condition_term(condition)
        entry = CONTENT_INDEX.get(normalized)
        if entry:
            # 🌐 Detect preferred language from Accept-Language header
            lang = (
                request.headers.get("accept-language", "en")
                .split(",")[0]
                .split("-")[0]
                .lower()
            )
            filename = entry.get(f"{lang}_filename", entry["filename"])
            path = os.path.join(EDU_DIR, filename)
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
            return PlainTextResponse(
                "No education material found for this condition.", status_code=404
            )

    return "Welcome to the Health Education Endpoint. Please provide a condition."
