import mimetypes
import fitz
from docx import Document
import re

def read_document(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)

    if mime_type == 'application/pdf':
        return read_pdf(file_path)
    elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return read_docx(file_path)
    elif mime_type == 'text/plain':
        return read_txt(file_path)
    else:
        return "File type not supported."

def read_pdf(file_path):
    """
    Reads the content of a PDF file.
    """
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()

    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    return text

def read_docx(file_path):
    """
    Reads the content of a DOCX file.
    """
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_txt(file_path):
    """
    Reads the content of a TXT file.
    """
    file_input = open(file_path, 'r', encoding='UTF-8')
    text = file_input.read()
    return text