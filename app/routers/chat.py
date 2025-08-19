from fastapi import APIRouter
from pydantic import BaseModel
from app.services.session_mem import SESSIONS
from app.services.cases_store import get_case
from app.services.patient_agent import get_patient_reply

router = APIRouter(prefix="/chat", tags=["chat"])

class Msg(BaseModel):
    case_id: str
    message: str

@router.post("/{session_id}")
def chat_with_patient(session_id: str, msg: Msg):
    case = get_case(msg.case_id)
    reply = get_patient_reply(case, SESSIONS[session_id].get("chat", []), msg.message)
    SESSIONS[session_id]["chat"].append({"role": "user", "msg": msg.message})
    SESSIONS[session_id]["chat"].append({"role": "patient", "msg": reply})
    return {"reply": reply}
