from app.services.llm_client import ask_llm_json

EVALUATOR_PROMPT = """You are a medical tutor... (system prompt here)"""

def evaluate_submission(case, student_answer):
    # Send to LLM (stubbed)
    return ask_llm_json(EVALUATOR_PROMPT, str(student_answer))
