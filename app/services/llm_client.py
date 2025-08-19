import os
import json

# Dummy LLM client for MVP
def ask_llm(system_prompt: str, user_prompt: str):
    # If you have an API key, here you'd call OpenAI/Groq/etc.
    # For MVP, return a fake safe response
    return f"(stub reply to: {user_prompt})"

def ask_llm_json(system_prompt: str, user_prompt: str):
    # Return fake evaluator JSON
    return {
        "diagnosis_score": 3,
        "tests_score": 2,
        "plan_score": 2,
        "feedback": ["Good attempt", "Missed one key test"],
        "learning_points": ["Inferior MI shows ST elevation in II, III, aVF."],
        "red_flags": False
    }
