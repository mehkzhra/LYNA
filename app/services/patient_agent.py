from app.services.llm_client import ask_llm

PATIENT_PROMPT = """You are a standardized patient... (system prompt here)"""

def get_patient_reply(case, transcript, user_msg):
    # Check if it's an investigation request
    for inv, result in case.get("investigations", {}).items():
        if inv.lower() in user_msg.lower():
            return result
    # Otherwise return LLM response (stubbed)
    return ask_llm(PATIENT_PROMPT, user_msg)
