from fastapi import APIRouter
import uuid
from app.services.session_mem import SESSIONS

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.post("")
def new_session():
    sid = str(uuid.uuid4())
    SESSIONS[sid] = {"chat": [], "revealed": []}
    return {"session_id": sid}
