from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(".env")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def evaluate_answer(question, answer):
    prompt = f"""
    Evaluate this interview answer.

    Question: {question}

    Answer: {answer}

    Give:
    Score out of 10
    Short feedback

    Format:
    8/10 - Good answer with relevant details
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
