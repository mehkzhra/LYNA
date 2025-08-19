from fastapi import APIRouter
from pydantic import BaseModel
from app.services.evaluator_agent import evaluate_submission
from app.services.cases_store import get_case
from app.services.session_mem import SESSIONS

router = APIRouter(prefix="/solve", tags=["solve"])

class SolveReq(BaseModel):
    case_id: str
    diagnosis: str
    tests: list[str]
    plan: str
    revealed_investigations: list[str]

@router.post("/{session_id}")
def solve_case(session_id: str, req: SolveReq):
    case = get_case(req.case_id)
    student = {
        "diagnosis": req.diagnosis,
        "tests": req.tests,
        "plan": req.plan,
        "revealed": req.revealed_investigations
    }
    result = evaluate_submission(case, student)
    if "attempts" not in SESSIONS[session_id]:
        SESSIONS[session_id]["attempts"] = []
    SESSIONS[session_id]["attempts"].append(result)
    return result
