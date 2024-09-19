import PyPDF2
from .text_detection import detect_text_plagiarism

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ''
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extract_text()
    return text

def detect_pdf_plagiarism(pdf_file1, pdf_file2):
    text1 = extract_text_from_pdf(pdf_file1)
    text2 = extract_text_from_pdf(pdf_file2)
    return detect_text_plagiarism(text1, text2)
