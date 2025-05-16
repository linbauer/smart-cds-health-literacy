# 📁 File: tests/test_normalize.py

from app.utils.normalize import normalize_condition_term


def test_alias_map_terms():
    assert normalize_condition_term("high blood pressure") == "hypertension"
    assert normalize_condition_term("sugar disease") == "diabetes"
    assert normalize_condition_term("reactive airway") == "asthma"


def test_fhir_term_map_terms():
    assert normalize_condition_term("type 2 diabetes mellitus") == "diabetes"
    assert normalize_condition_term("essential hypertension") == "hypertension"
    assert normalize_condition_term("chronic asthma") == "asthma"


def test_fallback_behavior():
    assert normalize_condition_term("asthma") == "asthma"
    assert normalize_condition_term("eczema") == "eczema"
