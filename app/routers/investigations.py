from fastapi import APIRouter
from pydantic import BaseModel
from app.services.cases_store import get_case
from app.services.session_mem import SESSIONS

router = APIRouter(prefix="/investigations", tags=["investigations"])

class RevealReq(BaseModel):
    name: str
    session_id: str

@router.get("/{case_id}")
def list_investigations(case_id: str):
    case = get_case(case_id)
    return list(case["investigations"].keys())

@router.post("/reveal/{case_id}")
def reveal_investigation(case_id: str, req: RevealReq):
    case = get_case(case_id)
    result = case["investigations"].get(req.name)
    SESSIONS[req.session_id]["revealed"].append(req.name)
    return {req.name: result}
