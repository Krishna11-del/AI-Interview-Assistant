import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")

def evaluate_answer(question, answer):

    prompt = f"""
    You are a technical interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer based on:
    1. Technical accuracy
    2. Completeness
    3. Clarity

    Give output exactly in this format:

    Score: X/10
    Feedback: <short feedback>
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"5/10 - Error: {e}"