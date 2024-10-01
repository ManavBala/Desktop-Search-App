import os
from PyPDF2 import PdfReader
from docx import Document
from datetime import datetime

def extract_text(file_path):
    text = ""
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    elif file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + '\n'
    # Add more file types if needed
    return text

def get_metadata(file_path):
    stats = os.stat(file_path)
    metadata = {
        'file_name': os.path.basename(file_path),
        'file_path': file_path,
        'size': stats.st_size,
        'creation_time': datetime.fromtimestamp(stats.st_ctime).isoformat(),
        'modification_time': datetime.fromtimestamp(stats.st_mtime).isoformat(),
    }
    return metadata
