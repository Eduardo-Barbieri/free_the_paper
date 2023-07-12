import io

import PyPDF2


def get_paper_content(pdf: io.BytesIO):
    reader = PyPDF2.PdfReader(pdf)
    for page in reader.pages:
        page = page.extract_text()
