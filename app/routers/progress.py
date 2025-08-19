from fastapi import APIRouter
from app.services.session_mem import SESSIONS

router = APIRouter(prefix="/progress", tags=["progress"])

@router.get("/{session_id}")
def progress(session_id: str):
    attempts = SESSIONS[session_id].get("attempts", [])
    if not attempts:
        return {"attempts": 0}
    avg = (sum(a["diagnosis_score"]+a["tests_score"]+a["plan_score"] for a in attempts)/len(attempts))
    weakest = min(["diagnosis","tests","plan"], key=lambda k: sum(a[f"{k}_score"] for a in attempts))
    return {"attempts": len(attempts), "average": avg, "weakest": weakest}
