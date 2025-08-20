# app/routers/chat.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.patient_agent import simulate_patient
from app.services.cases_store import get_case_by_id

router = APIRouter()

class ChatRequest(BaseModel):
    case_id: str
    message: str

@router.post("/chat")
def chat_with_patient(request: ChatRequest):
    case = get_case_by_id(request.case_id)
    if not case:
        return {"error": "Case not found"}

    reply = simulate_patient(case, request.message)
    return {"patient_reply": reply}
