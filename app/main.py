from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

# 🔹 Load environment variables
load_dotenv()

# 🔹 OpenAI client initialize
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 FastAPI app
app = FastAPI(title="Medical MVP Backend")

# 🔹 Request body schema
class ChatRequest(BaseModel):
    message: str

# 🔹 Root endpoint
@app.get("/")
def read_root():
    return {"message": "Medical MVP Backend is running 🚀"}

# 🔹 Chatbot endpoint
@app.post("/chat")
def chat_with_bot(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-5",
            messages=[
                {"role": "system", "content": "You are a patient describing your condition to a doctor. Speak like a patient."},
                {"role": "user", "content": request.message}
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content
        return {"reply": reply}

    except Exception as e:
        return {"error": str(e)}

