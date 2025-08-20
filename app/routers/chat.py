from fastapi import APIRouter
from pydantic import BaseModel
from openai import OpenAI
import os

router = APIRouter()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# User ke input ka model
class ChatRequest(BaseModel):
    user_message: str
    department: str

# Departments ka dummy data
medical_data = {
    "Cardiology": {
        "name": "John Doe",
        "age": 45,
        "gender": "Male",
        "symptoms": ["chest pain", "shortness of breath"],
        "medical_history": ["hypertension", "diabetes"],
    },
    "Neurology": {
        "name": "Sara Khan",
        "age": 32,
        "gender": "Female",
        "symptoms": ["headache", "dizziness"],
        "medical_history": ["migraine"],
    },
    "Orthopedics": {
        "name": "Ali Raza",
        "age": 50,
        "gender": "Male",
        "symptoms": ["joint pain", "swelling"],
        "medical_history": ["arthritis"],
    },
    "Dermatology": {
        "name": "Fatima Noor",
        "age": 28,
        "gender": "Female",
        "symptoms": ["skin rash", "itching"],
        "medical_history": ["eczema"],
    },
    "Pediatrics": {
        "name": "Baby Ahmed",
        "age": 3,
        "gender": "Male",
        "symptoms": ["fever", "cough"],
        "medical_history": ["seasonal flu"],
    },
}

@router.post("/chat")
async def chat_with_patient(request: ChatRequest):
    patient_info = medical_data.get(request.department, {})
    
    if not patient_info:
        return {"error": "Department not found!"}
    
    # Prompt GPT ko
    prompt = f"""
    Tum ek patient ho jiska data ye hai:
    {patient_info}

    Doctor tumse sawal karega aur tum patient ki tarah jawab do.
    Doctor ka sawaal: {request.user_message}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # free tier model, baad mein GPT-5 replace kar lena
        messages=[
            {"role": "system", "content": "Tum ek patient ho, sirf apne symptoms aur history ke base pe baat karo."},
            {"role": "user", "content": prompt},
        ]
    )

    return {"patient_response": response.choices[0].message.content}
