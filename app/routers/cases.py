from fastapi import APIRouter
from app.services.cases_store import CASES, get_case

router = APIRouter(prefix="/cases", tags=["cases"])

@router.get("")
def list_cases():
    return [{"id": c["id"], "patient": c["patient"]} for c in CASES]

@router.get("/{case_id}")
def case_detail(case_id: str):
    case = get_case(case_id)
    if not case: return {"error": "not found"}
    return {"id": case["id"], "patient": case["patient"], "investigations": list(case["investigations"].keys())}
