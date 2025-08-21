# app/routers/chat.py
from fastapi import APIRouter, HTTPException
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not set in your environment or .env file")

client = OpenAI(api_key=api_key)

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(payload: dict):
    try:
        question = payload.get("question")
        if not question:
            raise HTTPException(status_code=400, detail="No question provided")

        # GPT-5 chat completion
        response = client.chat.completions.create(
            model="gpt-5-mini",  # <- Use GPT-5 model
            messages=[{"role": "user", "content": question}]
        )

        answer = response.choices[0].message.content
        return {"answer": answer}

    except Exception as e:
        print("Error in chat endpoint:", e)  # logs error in console
        raise HTTPException(status_code=500, detail=str(e))
