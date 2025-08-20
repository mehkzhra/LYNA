# app/services/patient_agent.py
import json
from app.services import llm_client

def simulate_patient(department_data: dict, user_message: str) -> str:
    """
    Doctor (user) ke sawal ka jawab GPT-5 patient ke tor pe dega
    """
    patient_context = json.dumps(department_data["patient"])
    reply = llm_client.get_patient_reply(user_message, patient_context)
    return reply
