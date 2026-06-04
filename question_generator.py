# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# # Load .env file
# load_dotenv()

# # Configure Gemini
# genai.configure(
#     api_key=os.getenv("GEMINI_API_KEY")
# )

# # Gemini model
# model = genai.GenerativeModel("gemini-2.0-flash")

# def generate_questions(skills):

#     prompt = f"""
#     Generate exactly 6 technical interview questions based on these skills:

#     {', '.join(skills)}

#     Return only the questions.
#     """

#     try:
#         response = model.generate_content(prompt)

#         questions = []

#         for line in response.text.split("\n"):
#             line = line.strip()

#             if line:
#                 questions.append(line)

#         # Keep only first 6 questions
#         return questions[:6]

#     except Exception as e:

#         print("Gemini Error:", e)

#         # Fallback questions if Gemini quota is exhausted
#         return [
#             "What is Python and what are its advantages?",
#             "Explain the difference between a list and a tuple in Python.",
#             "What is SQL and what is a primary key?",
#             "What is Machine Learning and its types?",
#             "Explain the difference between a stack and a queue.",
#             "What is the time complexity of binary search?"
#         ]


from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv(".env")

print("API KEY =", os.getenv("GROQ_API_KEY"))

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_questions(resume_text):
    prompt = f"""
    Based on this resume, generate 6 interview questions.

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    text = response.choices[0].message.content

    return [q.strip() for q in text.split("\n") if q.strip()]
        ]
