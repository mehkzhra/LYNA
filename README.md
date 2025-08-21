# DocQuest — Clinical Reasoning Simulator
YOUR JOURNEY THROUGH REAL MEDICAL CASES--LEARN,PRACTICE AND GROW LIKE A DOCTOR.
> **Educational simulation only — not medical advice.**

DocQuest is a lightweight app that powers a virtual ward‑round experience for MBBS students. It provides realistic, safe case practice and an interactive “patient” chat, plus instant scoring/feedback on diagnosis, investigations, and initial management.

---

## ✨ Objectives

* Give students a **realistic but safe** space to practice clinical reasoning.
* Mirror **viva/OSCE** and ward‑round style workflows.
* Build confidence in **history‑taking, differential diagnosis, test ordering, and initial plan**.

---

## 🧭 How It Works (High‑Level)

DocQuest has two primary experiences:

1. **Case‑Based Learning**
   Students review a structured case (demographics → HPI → exam → optional labs) and submit:

* **Primary diagnosis**
* **Differential diagnoses** (optional )
* **Key investigations** (from a short list)
* **Initial management plan**

App returns:

* Correct diagnosis vs student’s answer
* Reasoning tips and investigation order
* A brief management overview

**Example case**

* 45‑year‑old male; 3‑month cough, fever, weight loss
* Sputum positive for AFB → **Pulmonary Tuberculosis**

2. **Patient‑Query Chatbot**
   A standardized **Patient Agent** answers only as a patient (no diagnoses). Students practice follow‑ups (onset, risk factors, red flags) and then submit their solution. An **Evaluator Agent** scores communication/diagnostic reasoning via a strict JSON schema.

---

## 🧩work Flow

* Load **50 synthetic cases** from `cases.json`.
* Provide simple toggles to **reveal prewritten investigations**.
* Collect the student’s **diagnosis / tests / plan**.
* Call the **Evaluator Agent** → return **scores + feedback bullets**.
* Keep **all state in memory** (no DB).

---

## 📁 Repository Layout (typical FastAPI style)

```
app/
  routers/           # API route modules (e.g., chat, cases, solve, investigations, sessions)
  services/          # business logic, agent clients, scoring utilities
  ...
requirements.txt     # Python dependencies
.env.example         # environment variables template
```

> Exact file names may vary; open each router to see the available paths.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI** (or similar) for the HTTP API
* **Uvicorn** for local dev server
* LLM provider of choice (OpenAI / Gemini / local via Ollama) wired through a thin client in `app/services/`

---

## 🚀 Getting Started

### 1) Clone

```bash
git clone https://github.com/mehkzhra/LYNA.git
cd LYNA
```

### 2) Create & Activate Virtual Environment

**Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install Dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure Environment

Copy the template and fill values:

```bash
# Windows
copy .env.example .env
# macOS/Linux
cp .env.example .env
```

Open `.env` and set keys like:

```
# Example — adapt to your provider
LLM_PROVIDER=openai          # openai | gemini | ollama
LLM_MODEL=gpt-4o-mini        # or your local model name
OPENAI_API_KEY=sk-xxxxx      # if using OpenAI
GEMINI_API_KEY=xxxx          # if using Gemini
OLLAMA_BASE_URL=http://localhost:11434 # if using Ollama
EVALUATOR_MODEL=gpt-4o-mini  # model used by Evaluator Agent
PATIENT_MAX_TOKENS=800
EVAL_MAX_TOKENS=600
```

> Keep `.env` **private**. Never commit secrets.

### 5) Run the Server

```bash
uvicorn app.main:app --reload --port 8000
```

Now open the interactive docs at:
`http://127.0.0.1:8000/docs`

---

## 🗂️ Cases Data (`cases.json`)

Minimal shape used by the LYNA:

```json
{
  "id": "C001",
  "specialty": "General Medicine",
  "patient": { "age": 45, "gender": "Male", "chief_complaint": "Chest pain for 2 hours" },
  "history_points": ["Pain radiates to left arm", "Sweating", "Nausea"],
  "exam_points": ["BP 90/60", "Pulse 110"],
  "investigations": {
    "ECG": "ST elevation in II, III, aVF",
    "Troponin I": "Positive"
  },
  "gold_diagnosis": "Acute Inferior Myocardial Infarction",
  "gold_minimal_tests": ["ECG", "Troponin I"],
  "learning_points": [
    "Inferior MI shows ST elevation in II, III, aVF.",
    "Avoid nitrates in suspected RV infarct; prioritize reperfusion pathways."
  ],
  "red_flags": ["Hypotension with chest pain", "Syncope"]
}
```

Place `cases.json` at the project root or wherever the code expects it (see `app/services/cases_store.py`).

---

## 🤖 Agent Prompts 

**Patient Agent — system**

> You are a standardized patient. Answer ONLY as the patient using details from the provided case memory. Do not suggest diagnoses, tests, or treatments. If the student asks for a test result that exists in the case, reveal exactly that result. If a test is not in the case, say “Not available.” Stay brief and realistic.

**Evaluator Agent — system**

> You are a medical tutor for an educational simulation (not real medical advice). Compare the student’s diagnosis, tests, and initial plan to the case’s gold answers. Score: diagnosis 0–4, tests 0–3, plan 0–3. Return STRICT JSON with keys: diagnosis\_score, tests\_score, plan\_score, feedback (array of short strings), learning\_points (array of short strings), red\_flags (boolean). Do not include any text outside JSON.

---

## 🔄 State Machine (Session)

Lightweight session states (in memory):

```
HOME → CASE_LIST → CASE_INTRO → (optional) INTERVIEW → SOLVE → EVAL
```
