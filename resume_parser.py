import PyPDF2

def extract_text(pdf_path):
    text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line.split()) >= 2 and len(line.split()) <= 4:
            return line

    return "Unknown Candidate"