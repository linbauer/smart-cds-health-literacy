# 📁 File: app/utils/normalize.py

ALIAS_MAP = {
    "high blood pressure": "hypertension",
    "sugar disease": "diabetes",
    "reactive airway": "asthma",
}

FHIR_TERM_MAP = {
    "type 2 diabetes mellitus": "diabetes",
    "type ii diabetes": "diabetes",
    "non-insulin-dependent diabetes mellitus": "diabetes",
    "essential hypertension": "hypertension",
    "chronic asthma": "asthma",
    "reactive airway disease": "asthma",
    "uncontrolled hypertension": "hypertension",
    "diabetes mellitus without complications": "diabetes",
}


def normalize_condition_term(raw_term: str) -> str:
    key = raw_term.lower()
    return ALIAS_MAP.get(key, FHIR_TERM_MAP.get(key, key))
