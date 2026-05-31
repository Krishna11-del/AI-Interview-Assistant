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

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_questions(resume_text):

    prompt = f"""
You are a technical interviewer.

Analyze this resume and generate exactly 6 personalized interview questions.

Resume:
{resume_text}

Rules:
- Questions must be based on projects, skills and technologies mentioned.
- Avoid generic definition questions.
- Make questions practical and interview-oriented.
- Return only the questions.
"""

    try:
        response = model.generate_content(prompt)

        questions = []

        for line in response.text.split("\n"):
            line = line.strip()

            if line:
                questions.append(
                    line.lstrip("1234567890.- ")
                )

        return questions[:6]

    except Exception as e:
        print("Gemini Error:", e)

        return [
            "Describe one project from your resume and explain your role.",
            "What was the biggest technical challenge you faced?",
            "Which technology mentioned in your resume are you most confident with?",
            "How would you improve one of your past projects?",
            "Explain a problem you solved using programming.",
            "What new skill are you currently learning?"
        ]