# SMART-on-FHIR Health Literacy CDS Tool (Archived v1)

**Status:** Archived – Portfolio Project  
**Repo:** [smart-cds-health-literacy](https://github.com/linbauer/smart-cds-health-literacy)  
**Tags:** `#cds` `#fhir` `#python` `#health-literacy` `#informatics` `#equity`  

---

## 📋 Summary

This project is a nurse-led clinical decision support (CDS) prototype designed to deliver plain-language, health-literate discharge instructions for chronic conditions (asthma, diabetes, hypertension) using **SMART-on-FHIR** principles. Built with **FastAPI**, the tool was designed to integrate with Epic/Cerner EHRs and explore how CDS systems can address **health literacy and equity gaps** in emergency department (ED) care.

The work represents a **completed learning milestone** and is no longer under active development. The codebase remains available as a portfolio artifact and potential foundation for future CDS prototypes.

---

## ✅ Features Completed

- 📘 `/education` endpoint serves plain-language Markdown content
- 🧠 Alias resolution for lay terms like `"sugar disease"` → `diabetes.md`
- 🌐 Planned localization via `Accept-Language` header (scaffolded)
- 🔎 `/patients` and `/search` endpoints scaffolded for future FHIR work
- 🧪 Unit tests for core endpoints (`education`, `normalize`)
- 📂 Organized modular backend: `routers`, `schemas`, `services`, `utils`

---

## 🚧 Features Planned but Not Implemented

- [ ] Live SMART-on-FHIR authentication and token context
- [ ] Real patient data from EHR (currently mocked)
- [ ] PDF export and multilingual fallback logic
- [ ] Frontend interface or embedded EHR iFrame
- [ ] Clinician-facing selection UI for common discharge topics

---

## 💻 Run the Project Locally

```bash
# Create and activate virtual environment
python3 -m venv fhir_env
source fhir_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
Open in browser:

- [http://localhost:8000/education?condition=asthma](http://localhost:8000/education?condition=asthma)
    
- [http://localhost:8000/docs](http://localhost:8000/docs)
    

---

## 🧠 Why This Project Matters

This CDS prototype was built to explore:

- How discharge education can be delivered in a way patients understand
    
- How to structure modular CDS tooling as a nurse without formal dev training
    
- How FHIR and health IT systems interact with clinical workflows
    
- How to prototype toward equity — not just tech completeness
    

---

## 🧑‍⚕️ Author

**Lindsay Bauer**  
Emergency Department RN | Health Equity Advocate | Informatics Learner  
Built this project to bridge frontline care with CDS development.

---

## 📄 License

MIT License — free for educational use, not production-ready.

---
