from reportlab.pdfgen import canvas

def create_report(skills, scores, final_score):

    pdf_file = "Interview_Report.pdf"

    c = canvas.Canvas(pdf_file)

    c.drawString(100, 800, "AI Interview Report")

    c.drawString(100, 770, f"Final Score: {final_score}/10")

    c.drawString(100, 740, "Skills Found:")

    y = 720

    for skill in skills:
        c.drawString(120, y, f"- {skill}")
        y -= 20

    c.drawString(100, y - 20, "Question Scores:")

    y -= 50

    for i, score in enumerate(scores, start=1):
        c.drawString(120, y, f"Question {i}: {score}/10")
        y -= 20

    c.save()

    return pdf_file