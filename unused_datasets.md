# Unused Datasets

These datasets from the original list are not included in the automated download script:

---

## SNOMED CT
- **Description:** Comprehensive clinical terminology for healthcare.
- **Why not included:** Full download requires a license; only browser access is free.
- **Link:** https://www.snomed.org/snomed-ct

---

## WHO ICD-11
- **Description:** International Classification of Diseases, 11th Revision.
- **Why not included:** Requires free API registration and manual API key setup.
- **Link:** https://icd.who.int/

---

## NHS 111
- **Description:** UK public health triage statistics and decision trees.
- **Why not included:** Only public statistics are available; full decision trees require a research agreement.
- **Link:** https://digital.nhs.uk/services/nhs-pathways

---

## openTriage
- **Description:** Research dataset for triage and clinical decision support.
- **Why not included:** Data available only upon request for research; not directly downloadable.
- **Link:** https://opentriage.org/ 

---

## Synthea
- **Description:** Synthetic patient health records for research and development.
- **Why not included:** SSL certificate issues prevent automated download in this environment. You can manually download from https://synthea.mitre.org/downloads
- **Link:** https://synthea.mitre.org/ 
---

# Used Datasets

These datasets are currently included in the `data/` directory and are being used for the RAG system.

---

## Medical Questions & Pairs
- **Directory:** `data/medical_questions_pairs/`
- **Description:** A dataset of medical question and answer pairs, likely for training conversational models or for retrieval.

---

## OpenFDA
- **Directory:** `data/openfda/`
- **Description:** Data from the OpenFDA project, which provides APIs and data about adverse events, drug labeling, and recalls. The `adverse_events.json` file is included.

---

## Symptom to Disease
- **Directory:** `data/symptom2disease/`
- **Description:** A CSV file mapping symptoms to potential diseases, useful for diagnostic aids.

---

## Open Patients
- **Directory:** `data/open_patients/`
- **Description:** Likely a dataset containing anonymized or synthetic patient records for analysis. 