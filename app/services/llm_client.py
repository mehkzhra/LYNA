# app/services/llm_client.py
from openai import OpenAI
import os

# Client initialize
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_patient_reply(user_message: str, patient_context: str) -> str:
    """
    GPT-5 ko call karega aur patient ki tarha reply karega
    """
    response = client.chat.completions.create(
        model="gpt-5",   # GPT-5 model use karna hai
        messages=[
            {"role": "system", "content": f"You are a patient. Here is your medical background: {patient_context}"},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
