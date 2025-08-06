# resume_parser.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    """
    Extracts all text from a PDF file (uploaded via Streamlit).
    """
    # Open the uploaded file using PyMuPDF
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    return text

