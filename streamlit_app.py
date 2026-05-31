import streamlit as st

from resume_parser import extract_text, extract_name
from skill_extractor import extract_skills
from question_generator import generate_questions
from evaluator import evaluate_answer
from report_generator import create_report

st.title("🤖 AI Interview Assistant")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    # Save uploaded PDF
    with open("uploaded_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract text
    text = extract_text("uploaded_resume.pdf")

    # Candidate name
    candidate_name = extract_name(text)
    st.success(f"Candidate Name: {candidate_name}")

    # Extract skills
    skills = extract_skills(text)

    st.subheader("Skills Found")

    for skill in skills:
        st.write("•", skill)

    # Generate Questions
    questions = generate_questions(skills)

    st.subheader("Interview Questions")

    answers = []

    for i, question in enumerate(questions):

        st.subheader(f"Question {i+1}")
        st.write(question)

        answer = st.text_area(
            f"Your Answer {i+1}",
            key=f"answer_{i}"
        )

        answers.append(answer)

    # Submit Button
    if st.button("Submit Interview"):

        st.subheader("📊 Results")

        scores = []

        for i, question in enumerate(questions):

            score = evaluate_answer(
                question,
                answers[i]
            )

            st.write(f"Question {i+1}: {score}")

            try:
                score_number = int(str(score).split("/")[0])
                scores.append(score_number)

            except:
                scores.append(5)

        final_score = round(
            sum(scores) / len(scores),
            1
        )

        st.success(
            f"Final Score: {final_score}/10"
        )

        # Create PDF Report
        report_file = create_report(
            skills,
            scores,
            final_score
        )

        with open(report_file, "rb") as f:

            st.download_button(
                "📄 Download Interview Report",
                f,
                file_name="Interview_Report.pdf"
            )
            